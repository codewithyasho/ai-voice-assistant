'''
Main pipeline for the voice assistant chatbot.
Flow: Audio Recording -> Speech-to-Text -> LLM Processing -> Text-to-Speech -> Play Audio
'''

import sounddevice as sd
from scipy.io.wavfile import write
from groq import Groq
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import asyncio
import edge_tts
from playsound3 import playsound
import os

# Load environment variables
load_dotenv()

# File paths
VOICE_OUTPUT_FILE = "voice-output.wav"
HUMAN_TEXT_FILE = "human-text.txt"
LLM_TEXT_FILE = "llm-text.txt"
AUDIO_OUTPUT_FILE = "audio_output.mp3"

# Audio recording parameters
SAMPLE_RATE = 44100  # samples per second
RECORD_SECONDS = 5   # seconds to record


def record_audio():
    """Step 1: Record audio from microphone"""
    print("\n[1/5] Recording audio...")
    print("Recording... Speak now!")

    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE, channels=1)
    sd.wait()  # wait until recording is done
    print("Finished recording.")

    # Save to file
    write(VOICE_OUTPUT_FILE, SAMPLE_RATE, audio)
    print(f"✓ Audio saved to {VOICE_OUTPUT_FILE}")


def speech_to_text():
    """Step 2: Convert speech to text using Whisper"""
    print("\n[2/5] Converting speech to text...")
    client = Groq()

    with open(VOICE_OUTPUT_FILE, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(VOICE_OUTPUT_FILE, file.read()),
            model="whisper-large-v3-turbo",
            temperature=0,
            response_format="verbose_json",
        )

    with open(HUMAN_TEXT_FILE, "w", encoding="utf-8") as f:
        f.write(transcription.text)

    print(f"✓ Transcription: {transcription.text}")
    print(f"✓ Saved to {HUMAN_TEXT_FILE}")
    return transcription.text


def process_with_llm():
    """Step 3: Process text with LLM"""
    print("\n[3/5] Processing with LLM...")
    model = init_chat_model("ollama:deepseek-v3.1:671b-cloud", temperature=0.2)

    with open(HUMAN_TEXT_FILE, "r", encoding="utf-8") as f:
        query = f.read()

    response = model.invoke(
        f"You are a helpful assistant. Answer the following query in very short: {query}")
    result = response.content

    with open(LLM_TEXT_FILE, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"✓ LLM response generated")
    print(f"✓ Saved to {LLM_TEXT_FILE}")
    return result


async def text_to_speech_async():
    """Step 4: Convert LLM response to speech"""
    print("\n[4/5] Converting text to speech...")

    with open(LLM_TEXT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    VOICE = "hi-IN-MadhurNeural"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(AUDIO_OUTPUT_FILE)

    print(f"✓ Audio generated and saved to {AUDIO_OUTPUT_FILE}")


def text_to_speech():
    """Wrapper for async text-to-speech function"""
    asyncio.run(text_to_speech_async())


def play_audio():
    """Step 5: Play the generated audio"""
    print("\n[5/5] Playing audio...")
    playsound(AUDIO_OUTPUT_FILE).wait()
    print("✓ Audio playback completed")


def main():
    """Main pipeline execution"""
    print("="*60)
    print("Voice Assistant Pipeline Started")
    print("="*60)

    try:
        # Step 1: Record audio
        record_audio()

        # Step 2: Speech to text
        transcription = speech_to_text()

        # Step 3: Process with LLM
        llm_response = process_with_llm()

        # Step 4: Text to speech
        text_to_speech()

        # Step 5: Play audio
        play_audio()

        print("\n" + "="*60)
        print("Pipeline completed successfully!")
        print("="*60)

    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        raise


if __name__ == "__main__":
    while True:
        main()

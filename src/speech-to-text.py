from groq import Groq
from dotenv import load_dotenv
load_dotenv()


client = Groq()
filename = "voice-output.wav"

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
        file=(filename, file.read()),
        model="whisper-large-v3-turbo",
        temperature=0,
        response_format="verbose_json",
    )
    print(transcription.text)

with open("human-text.txt", "w", encoding="utf-8") as f:
    f.write(transcription.text)

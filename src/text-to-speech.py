import asyncio
import edge_tts


with open("llm-text.txt", "r", encoding="utf-8") as f:
    TEXT = f.read()


VOICE = "hi-IN-MadhurNeural"

OUTPUT_FILE = "audio_output.mp3"


async def amain():
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

if __name__ == "__main__":
    asyncio.run(amain())


'''
Indian English Voices:
Female:
en-IN-NeerjaNeural
en-IN-AashiNeural
en-IN-AnanyaNeural
en-IN-KavyaNeural

male:
en-IN-PrabhatNeural


Indian Hindi Voices:
Female: hi-IN-SwaraNeural, hi-IN-KajalNeural, hi-IN-MadhurNeural
male:  hi-IN-MadhurNeural

Marathi: mr-IN-AarohiNeural (Female), mr-IN-ManoharNeural (Male)
'''

from playsound3 import playsound

AUDIO_OUTPUT_FILE = "audio_output.mp3"

sound = playsound(AUDIO_OUTPUT_FILE, block=False)
sound.wait()  # wait to finish
sound.stop()  # stop playback early

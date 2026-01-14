import sounddevice as sd
from scipy.io.wavfile import write

# Recording settings
sample_rate = 44100  # samples per second
duration = 5         # seconds to record

print("Recording...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()  # wait until recording is done
print("Recording finished.")

# Save to file
write("voice-output.wav", sample_rate, audio)
print("Saved as voice-output.wav")


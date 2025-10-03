import wave
import array
from pysstv.color import MartinM1
from PIL import Image

# Image load karo
img = Image.open("secret.png")

# SSTV object banao
sstv = MartinM1(img, 44100, 16)

# Generator ko list me collect karo aur PCM16 me convert karo
samples = array.array('h', sstv.gen_samples())  # 'h' = signed short (16-bit)

# WAV file create karo
with wave.open("secret.wav", "wb") as wav_file:
    wav_file.setnchannels(1)  # mono
    wav_file.setsampwidth(2)  # 16-bit
    wav_file.setframerate(44100)
    wav_file.writeframes(samples.tobytes())

print("✅ SSTV audio saved as secret.wav")

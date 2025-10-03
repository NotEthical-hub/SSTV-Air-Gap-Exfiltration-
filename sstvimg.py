import wave
import array
from pysstv.color import MartinM1
from PIL import Image

image_file = "myphoto1.jpg"   # apni image ka naam yahan daalo

# Image load + resize (SSTV ke liye standard size)
img = Image.open(image_file).resize((320, 256))

# SSTV encode
sstv = MartinM1(img, 44100, 16)
samples = array.array('h', sstv.gen_samples())

# WAV file save
with wave.open("output_sstv.wav", "wb") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(44100)
    wav_file.writeframes(samples.tobytes())

print("✅ SSTV audio ready: output_sstv.wav (Martin M1, 320x256)")


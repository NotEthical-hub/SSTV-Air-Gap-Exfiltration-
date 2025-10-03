from PIL import Image, ImageDraw, ImageFont  

# Text file padho
with open("secret.txt", "r") as f:
    text = f.read()

# Ek blank image banao
img = Image.new("RGB", (640, 480), color="black")
d = ImageDraw.Draw(img)

# Linux ke liye font path set karo
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font = ImageFont.truetype(font_path, 30)  # yaha 30 ko bada/chhota kar sakte ho

# Text likho image par
d.text((10, 10), text, fill=(255, 255, 255), font=font)

# Save image
img.save("secret.png")
print("✅ Text converted to image (secret.png)")


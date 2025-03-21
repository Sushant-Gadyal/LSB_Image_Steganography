import base64
import os
from PIL import Image

# Get the absolute path of the image
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get directory of encode.py
output_image_path = os.path.join(BASE_DIR, "../images/LSB_Spongbog_Image.png")

# Open the image
image = Image.open(output_image_path)
pixels = image.load()

# Extract binary data from the first row
extracted = ''

for x in range(image.width):
    r, g, b = pixels[x, 0]
    extracted += str(r & 1)
    extracted += str(g & 1)
    extracted += str(b & 1)

# Extract the length metadata (first 16 bits)
length_bits = extracted[:16]
message_length = int(length_bits, 2)  # Convert binary to integer

# Extract only the message bits
message_bits = extracted[16:16 + message_length]

# Convert message bits to bytes
byte_array = []
for i in range(0, len(message_bits), 8):
    byte = message_bits[i:i + 8]
    byte_array.append(int(byte, 2))

# Decode the Base64 message
decoded_message = ''.join(chr(byte) for byte in byte_array)
message = base64.b64decode(decoded_message).decode('utf-8')
print("Decoded Message:", message)

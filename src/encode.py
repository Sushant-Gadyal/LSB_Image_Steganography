import bitarray
import base64
import os
from PIL import Image

# Prepare the message
message = 'Sushant Gadyal'
bytes_message = message.encode('utf-8')
encoded_message = base64.b64encode(bytes_message).decode('utf-8')
ba = bitarray.bitarray()
ba.frombytes(encoded_message.encode('utf-8'))

# Convert to a bit array
bit_array = [int(i) for i in ba]
bit_array_length = len(bit_array)

# Convert the length of the bit array into binary (e.g., use 16 bits)
length_bits = list(map(int, bin(bit_array_length)[2:].zfill(16)))

# Append length bits at the start of the message
bit_array = length_bits + bit_array

# Get the absolute path of the image
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get directory of encode.py
input_image_path = os.path.join(BASE_DIR, "../images/Spongbog_Image.png")
output_image_path = os.path.join(BASE_DIR, "../images/LSB_Spongbog_Image.png")

# Encode the message into the image
im = Image.open(input_image_path)
im.save(output_image_path)
im = Image.open(output_image_path)
pixels = im.load()

width, height = im.size
i = 0

for x in range(width):
    r, g, b = pixels[x, 0]

    # Encode bits into RGB channels
    new_r = (r & ~1) | (bit_array[i] if i < len(bit_array) else 0)
    i += 1
    new_g = (g & ~1) | (bit_array[i] if i < len(bit_array) else 0)
    i += 1
    new_b = (b & ~1) | (bit_array[i] if i < len(bit_array) else 0)
    i += 1

    pixels[x, 0] = (new_r, new_g, new_b)
    if i >= len(bit_array):
        break

im.save(output_image_path)

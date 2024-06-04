from PIL import Image

# LSB_decryption
def lsb_decrypt(encoded_image, output_text):
    # Open the image
    img = Image.open(encoded_image)
    width, height = img.size
    
    # Extract the data
    binary_data = ""
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for i in range(3):
                binary_data += str(pixel[i] & 1)
    
    # Find EOF
    end_index = binary_data.find("00000000")
    if end_index != -1:
        binary_data = binary_data[:end_index]
    
    # Convert binary data into text
    bytes_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    text_data = bytes([int(byte, 2) for byte in bytes_data]).decode("utf-8")
    
    # save the text
    with open(output_text, "w") as file:
        file.write(text_data)
    
    print("LSB decryption completed. Output text saved as", output_text)


encoded_image = "/Users/mark/大学/ECEC/LSB/encode_image.png"
output_text = "hidden_text.txt"

lsb_decrypt(encoded_image, output_text)

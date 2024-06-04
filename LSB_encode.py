from PIL import Image
import os

#LSB_encryption
def lsb_encrypt(origin_image , text_file):

    img = Image.open(origin_image)
    width , height = img.size

    #Open the text file and read the data
    with open(text_file , "rb") as file:
        data = file.read()

    #Convert the text into binary version
    binary_data = ''.join(format(byte, '08b') for byte in data)
    data_length = len(binary_data)

    #Check if the image is big enough for containing all the data
    if width * height * 3 < data_length:
        print("Error: Image size too small to hide data.")
        return
    
    #Write the data to each of the image Least significant bit.
    index = 0
    for y in range(height):
        for x in range(width):
            pixel = []
            pixel = list(img.getpixel((x, y)))
            for i in range(3):
                if index < data_length:
                    pixel[i] = pixel[i] & ~1 | int(binary_data[index])
                    index += 1
            img.putpixel((x, y), tuple(pixel))

    # Find the currenct directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Output the image name
    output_image = os.path.join(current_directory, "output_image.png")

    # Save the encrypted image
    img.save(output_image)
    print("LSB encryption completed. Output image saved as:", output_image)

picture = "/Users/mark/大学/ECEC/LSB/万恶之源.png"
text = "/Users/mark/大学/ECEC/LSB/encode_text.txt"

lsb_encrypt(picture , text)

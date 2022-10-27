# Imports PIL module 
from PIL import Image

# open image lena_cor.bmp
image = Image.open("lena_cor.bmp")

n = 7
while (n > 0):
    image_quantized = image.quantize(2**n)
    print("Image quantized to " + str(n) + " bits")
    image_quantized.show()
    n -= 1
    # wait for user to close the image
    input("Press Enter to continue...")

image_gray = Image.open("lena_gray.bmp")

n = 7
while (n > 0):
    image_gray_quantized = image_gray.quantize(2**n)
    print("Image quantized to " + str(n) + " bits")
    image_gray_quantized.show()
    n -= 1
    # wait for user to close the image
    input("Press Enter to continue...")

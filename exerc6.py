# Imports PIL module 
from PIL import Image

# open image lena_cor.bmp
image = Image.open("lena_cor.bmp")

# create a image in gray scale based on the average of the 3 channels
image_gray = image.convert("L")

# save the image in gray scale
image_gray.save("lena_gray_wj.bmp")
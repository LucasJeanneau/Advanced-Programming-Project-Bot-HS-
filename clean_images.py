from PIL import Image
from PIL import ImageFilter
import os
  
## Crop Taunt images

# path of the folder containing the images
inPath ="C:\\Users\lucas\Desktop\HS_Project\IM_TAUNT"
  
# path of the folder that will contain the modified image
outPath ="C:\\Users\lucas\Desktop\HS_Project\IM_CROP_TAUNT"

## box is the part of the image that i want to save 
box = (55,40,120,120)

for imagePath in os.listdir(inPath):
    inputPath = os.path.join(inPath, imagePath)
    img = Image.open(inputPath)
    fullOutPath = os.path.join(outPath, 'crop'+imagePath)
    img.resize((188,259)).crop(box).save(fullOutPath)
    
## This loop allows to crop all images from the folder IM_TAUNT and save them into the folder "IM_CROP_TAUNT"

## Then, I crop all cards

inPath ="C:\\Users\lucas\Desktop\HS_Project\IM_ALL"
outPath ="C:\\Users\lucas\Desktop\HS_Project\IM_CROP_ALL"


for imagePath in os.listdir(inPath):
    inputPath = os.path.join(inPath, imagePath)
    img = Image.open(inputPath)
    fullOutPath = os.path.join(outPath, 'crop'+imagePath)
    img.resize((188,259)).crop(box).save(fullOutPath)
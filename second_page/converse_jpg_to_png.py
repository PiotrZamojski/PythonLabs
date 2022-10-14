import os
from PIL import Image

def jpgToPdfConverter():
    im1 = Image.open('C:\\Users\\zamoj\\Desktop\\python\\PythonLabs\\python_photos\\first_photo.jpg')
    im1.save('C:\\Users\\zamoj\\Desktop\\python\\PythonLabs\\python_photos\\first_photo_converter.png')


if __name__ == '__main__':
   jpgToPdfConverter()
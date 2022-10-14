import os
from PIL import Image

def findAllJpgFIles():
    path = os.path.realpath('C:\Programowanie w Pythonie\AK_pon_11_20\JpgIntoPng')
    for root, d_names, f_names in os.walk(path):
        print(root, d_names, f_names)
        for i in f_names:
            print(i)


def jpgToPdfConverter():
    path = os.path.realpath('C:\Programowanie w Pythonie\AK_pon_11_20\JpgIntoPng')
    for root, d_names, f_names in os.walk(path):
        print(root, d_names, f_names)
        for i in f_names:
            print(i)


if __name__ == '__main__':
    findAllJpgFIles()
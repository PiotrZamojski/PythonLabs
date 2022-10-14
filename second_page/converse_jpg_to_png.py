import os
from PIL import Image

def findAllJpgFIles():
    path = os.path.realpath('C:\Users\zamoj\Desktop\python\PythonLabs')
    for root, d_names, f_names in os.walk(path):
        print(root, d_names, f_names)
        for i in f_names:
            print(i)


def jpgToPdfConverter():
    path = os.path.realpath('C:\Users\zamoj\Desktop\python\PythonLabs')
    for root, d_names, f_names in os.walk(path):
        print(root, d_names, f_names)
        for i in f_names:
            print(i)


if __name__ == '__main__':
    findAllJpgFIles()
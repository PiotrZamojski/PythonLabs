import os

def numberOfFiles():
    print("Give path")
    path = input()
    amount = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    print(amount)

if __name__ == '__main__':
    numberOfFiles()
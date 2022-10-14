from random import randint


def dotProduct(a,b):
    for i in range(len(a)):
        result = a[i]*b[i]
    print(result)

if __name__ == '__main__':
    a = [1,2,12,4]
    b = [2,4,2,8]
    dotProduct(a,b)
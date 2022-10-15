from cgitb import reset
from random import randint
import re


def newMatrix(rows, cols):
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])
    return matrix

def generateValueMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
           m[i][j] = randint(0,4)
    for value in m:
        print(value)
    print("\n")

def matrixDeterminant(a):
    if len(a) == 1:
        result = a[0][0]
        print(result)
    elif len(a) == 2:
        result = a[0][0]*a[1][1] - a[1][0]*a[0][1]
        print(result) 
    else:
        result = 0
        for j in range(len(a)):
            result += pow(-1,j)*a[0][j]
            print(type(matrixDeterminant(getMatrixMinor(a,j))))
        print(result)

def getMatrixMinor(m,j):
    x =[row[:j] + row[j+1:] for row in (m[:0]+m[1:])]
    return 

if __name__ == '__main__':
    a = newMatrix(3,3)
    generateValueMatrix(a)
    matrixDeterminant(a)
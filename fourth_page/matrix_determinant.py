from random import randint
import numpy as np

def newMatrix(rows, cols):
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])
    return matrix

def generateValueMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
           m[i][j] = randint(0,2)
    for value in m:
        print(value)
    print("\n")

def calculateDet(matrix):
    return np.linalg.det(matrix)

if __name__ == '__main__':
    a = newMatrix(3,3)
    generateValueMatrix(a)
    print(calculateDet(a))
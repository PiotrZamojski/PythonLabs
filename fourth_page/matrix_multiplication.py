from random import randint


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

def matrixMultiply(a,b):
    result = newMatrix(len(a), len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    for value in result:
        print(value)

if __name__ == '__main__':
    a = newMatrix(8,8)
    b = newMatrix(8,8)
    generateValueMatrix(a)
    generateValueMatrix(b)
    matrixMultiply(a,b)
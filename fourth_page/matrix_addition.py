from random import randint



def newMatrix(rows, cols):
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])
    return matrix

def generateValueMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
           m[i][j] = randint(0,1)
    for value in m:
        print(value)
    print("\n")

def matrixAddition(a,b):
    result = newMatrix(len(a), len(a[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    for value in result:
        print(value)

if __name__ == '__main__':
    a = newMatrix(8,8)
    b = newMatrix(8,8)
    generateValueMatrix(a)
    generateValueMatrix(b)
    matrixAddition(a,b)
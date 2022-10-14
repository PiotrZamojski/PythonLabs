from random import randint


def bubbleSort(numbers):
    length = len(numbers)
    for i in range(length-1):
        for j in range(length-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(numbers)

if __name__ == '__main__':
    numbers = []
    for i in range(50):
        x = randint(0,100)
        numbers.append(x)
    bubbleSort(numbers)
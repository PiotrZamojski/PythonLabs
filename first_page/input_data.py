def data():
    inputData = ("name", "surname", "Date of birth")
    userData = []
    for i in inputData:
        print("Give "+i)
        userData.append(input())
    print(userData)


if __name__ == '__main__':
    data()

def encode(code):
    print("Give code to encode")
    inputCode = input()
    if inputCode == code:
        print("You provide good code")
        return True
    else:
        print("Wrong code")
        return False


if __name__ == '__main__':
    print("Give first code")
    exampleCode = input()
    while True:
        isValid = encode(exampleCode)
        if isValid == True:
            pass
        else:
            break

def deleteString():
    dictionary = ["się", " i ", "oraz", "nigdy", "dlaczego"]
    pathIn = "C:\\Users\\zamoj\\Desktop\\python\\PythonLabs\\third_page\\warszawa.txt"
    pathOut = "C:\\Users\\zamoj\\Desktop\\python\\PythonLabs\\third_page\\warszawa_delete_string.txt"
    fileIn = open(pathIn,"r",encoding="utf-8")
    fileOut = open(pathOut, "w+",encoding="utf-8")
    for line in fileIn:
        for word in dictionary:
            line = line.replace(word, "")
        fileOut.write(line)
    fileIn.close()
    fileOut.close()

if __name__ == '__main__':
    deleteString()
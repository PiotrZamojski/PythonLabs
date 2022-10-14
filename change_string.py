def changeString():
    dictionary= {
        " i ": " a ",
        " oraz ":" i ",
        " nigdy ":" prawie nigdy ",
        " dlaczego ":" czemu "
    }
    pathIn = "C:\\Users\\zamoj\\Desktop\\python\\PythonLabs\\third_page\\warszawa.txt"
    pathOut = "C:\\Users\\zamoj\\Desktop\\python\\PythonLabs\\third_page\\warszawa_change_string.txt"
    fileIn = open(pathIn,"r",encoding="utf-8")
    fileOut = open(pathOut, "w+",encoding="utf-8")
    for line in fileIn:
        for key, value in dictionary.items():
            line = line.replace(key, value)
        fileOut.write(line)
    fileIn.close()
    fileOut.close()

if __name__ == '__main__':
    changeString()
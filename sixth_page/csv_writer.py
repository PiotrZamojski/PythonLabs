import pandas
import csv as csvFile

def csv():
    pathIn = ".\\sixth_page\\example.csv"

    print("-- File CSV --")
    data = pandas.read_csv(pathIn,  encoding='unicode_escape')
    print(data)
    print("Enter new task(new) or delete task(delete): ")
    task = input()
    if task == "delete":
        print("Enter delete column name: ")
        column = input()
        data.drop(column, inplace=True, axis=1)
        data.to_csv(pathIn, index=False, header=True)
        print("-- File CSV  --")
        data = pandas.read_csv(pathIn)
        print(data)
        return
    elif task == "new":
        print("Provide row")
        row = input()
        print("Provide column")
        column = input()
        newData = pandas.DataFrame([[row]], columns=[column])
        data = data.join(newData, lsuffix='_caller', rsuffix='_other')
        data.to_csv(pathIn, index=False, sep=';')
        print("-- File CSV  --")
        data = pandas.read_csv(pathIn)
        print(data)
        return
    else:
        print("Nothing done")
        return
if __name__ == '__main__':
    csv()
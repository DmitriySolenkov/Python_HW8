import csv


def printTXT():
    f = open('phonebook.txt', 'r')
    line = f.readline()
    while line != '':
        print(line)
        line = f.readline()
    print('Конец TXT-справочника')
    f.close


def printCSV():
    with open('phonebook.csv', 'r') as reader:
        for row in reader.readlines():
            print(row)
    print('Конец CSV-справочника')

import csv


def searchNoteTXT(request):
    f = open('phonebook.txt', 'r')
    request = request.lower()
    count = 0
    line = f.readline()
    lineLow = line.lower()
    while line != '':
        if request in lineLow:
            print(line)
            count += 1
        line = f.readline()
        lineLow = line.lower()
    if count == 0:
        print('Совпадений не обнаружено')
    else:
        print('Конец TXT-справочника')
    f.close


def searchNoteCSV(request):
    request = request.lower()
    count = 0
    with open('phonebook.csv', 'r') as reader:
        for row in reader.readlines():
            rowLow = row.lower()
            if request in rowLow:
                count += 1
                print(row)
        if count == 0:
            print('Совпадений не обнаружено')
        else:
            print('Конец CSV-справочника')

import csv


def noteWritingTXT(list):
    f = open('phonebook.txt', 'a')
    note = list[0]+' | '+list[1]+' | '+list[2]+' | '+list[3]+' | '+list[4]
    f.write(note)
    f.write('\n')
    f.close


def noteWritingCSV(list):
    with open("phonebook.csv", mode="a", encoding='utf-8') as w_file:
        filewriter = csv.writer(w_file, delimiter="|", lineterminator="\r")
        filewriter.writerow([list[0], list[1], list[2], list[3], list[4]])

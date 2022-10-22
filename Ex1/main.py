import input as i
import writing as w
import search as s
import print as p


def Mode(message):
    mode = int(input(message))
    if 1 <= mode <= 3:
        return mode
    else:
        print('Выбрана некорректная функция!')
        mode = Mode()
        return mode


mode = Mode('Для записи нового абонента в справочник введите 1\nДля нахождения определенного абонента в справочнике введите 2\nДля вывода всего справочника построчно введите 3:')
if mode == 1:
    modeInput = Mode(
        'Для сохранения записи в txt-файле введите 1\nДля сохранения записи в csv-файле введите 2\nДля сохранения записи в обоих файлах введите 3:')
    note = list(i.addNote())
    if modeInput == 1:
        w.noteWritingTXT(note)
    elif modeInput == 2:
        w.noteWritingCSV(note)
    else:
        w.noteWritingTXT(note)
        w.noteWritingCSV(note)
elif mode == 2:
    modeSearch = Mode(
        'Для поиска записи в txt-файле введите 1\nДля поиска записи в csv-файле введите 2\nДля поиска записи в обоих файлах введите 3:')
    request = input('Введите запрос для поиска совпадений:')
    if modeSearch == 1:
        s.searchNoteTXT(request)
    elif modeSearch == 2:
        s.searchNoteCSV(request)
    else:
        s.searchNoteTXT(request)
        s.searchNoteCSV(request)
else:
    modePrint = Mode(
        'Для вывода txt-справочника введите 1\nДля вывода csv-справочника введите 2\nДля вывода обоих справочников введите 3:')
    if modePrint == 1:
        p.printTXT()
    elif modePrint == 2:
        p.printCSV()
    else:
        p.printTXT()
        p.printCSV()

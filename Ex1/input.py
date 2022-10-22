def addText(message):
    text = input(message)
    check = ('')
    count = 0
    for i in text:
        if i == ' ':
            count += 1
    if check == text or count == len(text):
        print('Пустая запись не может быть создана!')
        text = addText(message)
        return text
    else:
        return text


def addNumber(message, ch):
    number = input(message)
    check = ('')
    count = 0
    for i in number:
        if i == ' ':
            count += 1
    boolcheck = True
    if check == number or count == len(number):
        print('Пустая запись не может быть создана!')
        number = addNumber(message, ch)
        return number
    else:
        for char in number:
            if char.isdigit() or char == ch:
                boolcheck = True
            else:
                boolcheck = False
                break
    if boolcheck == True:
        return number
    else:
        print('Проверьте корректность ввода номера!')
        number = addNumber(message, ch)
        return number


def addNote():
    note = []
    note.append(addText('Введите фамилию, имя, отчество нового абонента:'))
    note.append(
        addNumber('Введите дату рождения нового абонента(в формате ДД.ММ.ГГГГ):', '.'))
    note.append(addNumber('Введите номер телефона нового абонента:', '+'))
    note.append(addText('Введите описание номера нового абонента:'))
    note.append(addText('Введите адрес нового абонента:'))

    return note

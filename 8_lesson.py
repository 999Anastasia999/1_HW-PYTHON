# Урок 8. Работа с файлами

# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона
# данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программане должна быть линейной

def inputText():
    with open('tel_dir.txt', 'a', encoding='utf-8') as data: # конструкция позволяет открывать-закрвать файл авто
        surname = data.write(input('Введите фамилию '))
        data.write(' ')
        name = data.write(input('Введите имя '))
        data.write(' ')
        fathername = data.write(input('Введите отчество '))
        data.write(' ')
        phoneNumber = data.write(input('Введите номер телефона '))
        data.write('\n')


def printText():
    data = open('tel_dir.txt', 'r')
    for line in data:
        print(line)                       # <class 'str'>
    data.close()

def checkText(userInfo):
    path = 'tel_dir.txt'
    data = open('tel_dir.txt', 'r')

    for line in data.readlines():
        if userInfo in line:
            print(line)
    data.close()


inputText()
printText()
checkText(input('Введите данные '))

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
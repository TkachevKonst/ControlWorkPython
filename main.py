import datetime
import os


def id(data):
    id = 0
    if os.path.exists(data):
        if os.stat(data).st_size == 0:
            return 1
        with open(data, 'r', encoding='UTF8') as dt:
            lines = dt.readlines()
            lines1 = lines[::4]
            for line in lines1:
                line1 = line.split(' : ')
                line1 = line1[0].split(' ')
                if id < int(line1[1]):
                    id = int(line1[1])
            return id + 1
    return 1

def none_fail(data):
    if os.path.exists(data):
        if os.stat(data).st_size == 0:
            print("Заметок не найдено. Сделайте запись")
            write_new(data)


def sort_list_date(data):
    with open(data,'r',encoding='UTF8') as dt:
        lt = list()
        lines = dt.readlines()
        lines1 = lines[2::4]
        lines1.sort()
        for line in lines1:
            lt.append(lines[lines.index(line)-2])
            lt.append(lines[lines.index(line)-1])
            lt.append(lines[lines.index(line)])
            lt.append('***\n')
    with open(data, 'w', encoding='UTF8') as dt:
        for line in lt:
            dt.write(line)


def search_id(data, item):
    with open(data, 'r', encoding='utf8') as dt:
        lines = dt.readlines()
        lines1 = lines[::4]
        for line in lines1:
            if item in line:
                return lines1.index(line)
        return print("Не верно ввели данные.")

def search_date(data):
    none_fail(data)
    count = 0
    item = input('Введите дату заметки в формате дд.мм(Например 15.05 - 15 мая)\n')
    with open(data, 'r', encoding='utf8') as dt:
        lines = dt.readlines()
        lines1 = lines[2::4]
        for line in lines1:
            if item in line:
                count += 1
                print(lines[4 * lines1.index(line)] + lines[1 + 4 * lines1.index(line)] + lines[
                    2 + 4 * lines1.index(line)])
        if count == 0: print("На данную дату (" + item + ") нет записей")


def write_new(data):
    new_str0 = str(id(data))
    new_str1 = input('Заголовок: ')
    new_str2 = input('Заметка: ')
    new_str3 = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    with open(data, 'a', encoding='utf8') as dt:
        dt.write('id ' + new_str0 + ' : ')
        dt.write(new_str1 + '.\n')
        dt.write(new_str2 + '\n')
        dt.write(new_str3 + '\n***\n')


def change_note(data):
    none_fail(data)
    item = input('какую запись изменить (введите id): ')
    item_type = int(input('Введите номер что хотите изменить (1-Заголовок, 2-Заметка): '))
    index = search_id(data, item)
    with open(data, 'r', encoding='utf8') as dt:
        lines = dt.readlines()
        match item_type:
            case 1:
                line1 = lines[4 * index].split(' : ')
                line1[1] = input('Введите изменение: ') + '\n'
                line1 = ' : '.join(line1)
                lines[4 * index] = line1
                lines[2 + 4 * index] = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")) + '\n'
            case 2:
                lines[1 + 4 * index] = input('Введите изменение: ') + '\n'
                lines[2 + 4 * index] = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")) + '\n'
        with open(data, 'w', encoding='utf8') as dt:
            for line in lines:
                dt.write(line)
    sort_list_date(note)

def read_one(data):
    none_fail(data)
    item = input('какую запись вывестив в консоль (введите id): ')
    index = search_id(data,item)
    with open(data, 'r', encoding='UTF8') as dt:
        lines = dt.readlines()
        print(lines[4*index]+lines[1+4*index]+lines[2+4*index])

def read_all(data):
    none_fail(data)
    with open(data, 'r', encoding='UTF8') as dt:
        print(dt.read().strip())

def delete_note_one(data):
    none_fail(data)
    item = input('Какую запись удалить (введите id): ')
    index = search_id(data, item)
    with open(data, 'r', encoding='utf8') as dt:
        lines = dt.readlines()
        lines.pop(4*index)
        lines.pop(4*index)
        lines.pop(4*index)
        lines.pop(4*index)
    with open(data, 'w', encoding='utf8') as dt:
        for line in lines:
            dt.write(line)

def delete_note(data):
    with open(data, 'r', encoding='utf8') as dt:
        lines = dt.readlines()
        lines.clear()
    with open(data, 'w', encoding='utf8') as dt:
        for line in lines:
            dt.write(line)


def main(data):
    a = 1
    while (a == 1):
        print('Введите номер операции, где: ',
                '1-Новая заметка',
                '2-Редактирование заметки',
                '3-Вывод всех заметок',
                '4-Вывод одной заметки',
                '5-Поиск заметки по дате',
                '6-Удаление одной заметки',
                '7-Удаление всех заметок',
                '0 - выход : ', sep='\n', end='\n')
        match input():
            case '1':
                write_new(data)
            case '2':
                change_note(data)
            case '3':
                read_all(data)
            case '4':
                read_one(data)
            case '5':
                search_date(data)
            case '6':
                delete_note_one(data)
            case '7':
                delete_note(data)
            case '0':
                print('Good bay!!!')
                a=2
            case _:
                print('Ошибка при вводе')
                a=2


note = "note.csv"
main (note)


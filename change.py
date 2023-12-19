import datetime

import exception
import search
import sort


def change_note(data):
    exception.none_fail(data)
    item = input('какую запись изменить (введите id): ')
    item_type = int(input('Введите номер что хотите изменить (1-Заголовок, 2-Заметка): '))
    index = search.search_id(data, item)
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
    sort.sort_list_date(data)
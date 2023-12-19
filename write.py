import datetime


def write_new(data):
    new_str0 = str(id.count(data))
    new_str1 = input('Заголовок: ')
    new_str2 = input('Заметка: ')
    new_str3 = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    with open(data, 'a', encoding='utf8') as dt:
        dt.write('id ' + new_str0 + ' : ')
        dt.write(new_str1 + '.\n')
        dt.write(new_str2 + '\n')
        dt.write(new_str3 + '\n***\n')

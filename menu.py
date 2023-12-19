import change
import delete
import read
import search
import write


def main_menu (data):
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
                write.write_new(data)
            case '2':
                change.change_note(data)
            case '3':
                read.read_all(data)
            case '4':
                read.read_one(data)
            case '5':
                search.search_date(data)
            case '6':
                delete.delete_note_one(data)
            case '7':
                delete.delete_note(data)
            case '0':
                print('Good bay!!!')
                a=2
            case _:
                print('Ошибка при вводе')
                a=2





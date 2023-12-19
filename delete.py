import exception
import search


def delete_note_one(data):
    exception.none_fail(data)
    item = input('Какую запись удалить (введите id): ')
    index = search.search_id(data, item)
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
import exception
import search

def read_one(data):
    exception.none_fail(data)
    item = input('какую запись вывестив в консоль (введите id): ')
    index = search.search_id(data,item)
    with open(data, 'r', encoding='UTF8') as dt:
        lines = dt.readlines()
        print(lines[4*index]+lines[1+4*index]+lines[2+4*index])

def read_all(data):
    exception.none_fail(data)
    with open(data, 'r', encoding='UTF8') as dt:
        print(dt.read().strip())
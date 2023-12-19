import os


def count(data):
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
import exception


def search_id(data, item):
    with open(data, 'r', encoding='utf8') as dt:
        lines = dt.readlines()
        lines1 = lines[::4]
        for line in lines1:
            if item in line:
                return lines1.index(line)
        return print("Не верно ввели данные.")

def search_date(data):
    exception.none_fail(data)
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
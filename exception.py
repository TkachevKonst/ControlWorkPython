import os


def none_fail(data):
    if os.path.exists(data):
        if os.stat(data).st_size == 0:
            print("Заметок не найдено. Сделайте запись")
            write_new(data)
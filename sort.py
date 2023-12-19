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
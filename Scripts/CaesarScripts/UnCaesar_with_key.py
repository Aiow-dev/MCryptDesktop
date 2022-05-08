def UnCaesar_with_key(shifr, key_num, key_word):  # "зитдркыщ оыэкиы", ,5, "работа"
    shifr = shifr.lower()                         # прилетаю завтра
    table = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ''
    shifr_table = sum(key_word, shifr_table)
    shifr_table = sum(table, shifr_table)
    for i in range(0,key_num):
        shifr_table = shifr_table[-1] + shifr_table[0:-1:]
    message = ""
    for i in shifr:
        if i not in table:
            message += i
        else:
            message += table[shifr_table.find(i)]
    return message


def sum(string, table):
    for i in string:
        if table.find(i) == -1:
            table += i
    return table

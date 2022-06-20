def Caesar_with_key(message, key_num, key_word):   # "ПРИЛЕТАЮ ЗАВТРА",5, "работа"
    message = message.lower()                      # Вывод зитдркыщ оыэкиы
    table = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ''
    shifr_table = sum(key_word, shifr_table)
    shifr_table = sum( table, shifr_table)
    for i in range(0,key_num):
        shifr_table = shifr_table[-1] + shifr_table[0:-1:]
    shifr = ""
    for i in message:
        if i not in table:
            shifr += i
        else:
            shifr += shifr_table[table.find(i)]
    return shifr, shifr_table


def sum(string, table):
    for i in string:
        if table.find(i) == -1:
            table += i
    return table


if __name__ == '__main__':
    print(Caesar_with_key('ПРИЛЕТАЮ ЗАВТРА', 5, 'работа'))

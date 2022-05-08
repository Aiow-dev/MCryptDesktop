def Caesar_Classic(message, key):   # "ПРИЛЕТАЮ ЗАВТРА",3
    message = message.lower()       # Вывод: тулозхгб кгехуг
    table = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ""
    for i in range(key, 33 + key):
        m = i % 33
        shifr_table += table[m]
    shifr = ""
    for i in message:
        if i not in table:
            shifr += i
        else:
            shifr += shifr_table[table.find(i)]
    return shifr, table, shifr_table


if __name__ == '__main__':
    print(Caesar_Classic('ПРИЛЕТАЮ ЗАВТРА', 3))

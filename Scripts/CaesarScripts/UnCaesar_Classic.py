def UnCaesar_Classic(shifr, key):   # "тулозхгб кгехуг",3
    shifr = shifr.lower()           # Вывод: прилетаю завтра
    table = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ""
    for i in range(key, 33 + key):
        m = i % 33
        shifr_table += table[m]
    message = ""
    for i in shifr:
        if i not in table:
            message += i
        else:
            message += table[shifr_table.find(i)]
    return message

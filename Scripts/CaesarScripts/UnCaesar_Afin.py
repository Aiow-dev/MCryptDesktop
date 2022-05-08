def UnCaesar_Afin(shifr, key_a, key_b):     # "адерхлвъ бвйлдв",4,2
    if key_a < key_b:                       # Вывод: прилетаю завтра
        return "Не выполнены условия шифрования (a<b)"
    shifr = shifr.lower()
    table = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ''
    for i in range(0,33):
        rang = (key_a * i + key_b) % 33
        shifr_table += table[rang]
    message = ''
    for i in shifr:
        if i not in table:
            message += i
        else:
            message += table[shifr_table.find(i)]
    return message

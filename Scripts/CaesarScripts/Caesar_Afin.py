def Caesar_Afin(message, key_a, key_b):    # "ПРИЛЕТАЮ ЗАВТРА",4,2
    if key_a < key_b:                      # Вывод адерхлвъ бвйлдв
        return "Не выполнены условия шифрования (a<b)"
    message = message.lower()
    table = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ''
    for i in range(0,33):
        rang = (key_a * i + key_b) % 33
        shifr_table += table[rang]
    shifr = ''
    for i in message:
        if i not in table:
            shifr += i
        else:
            shifr += shifr_table[table.find(i)]
    return shifr, table, shifr_table

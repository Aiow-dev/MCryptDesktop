from Core.Helpers import table_helpers


def UnKeyPermutation(shifr, row, column,
                     key):  # Входные данные: "ДВПЕМСЕПРТОЕНОИАГДЬЛЛЮОЬ", row = 4, column = 6, key = "КОРОВА"
    clear_shifr = ''.join(shifr.split(' ')).upper()  # Выходные данные: "ПРИЛЕТАЮСЕДЬМОГОВПОЛДЕНЬ"

    if (len(clear_shifr) != row * column):
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"

    mas = [[] for _ in range(column)]

    for i in range(column):
        for k in range(row):
            mas[i].insert(k, clear_shifr[i + column * k])

    cipher = {}
    index_ch = 0
    for index, ch in enumerate(key.lower()):
        if ch in cipher:
            cipher[ch + str(index_ch)] = index_ch
        else:
            cipher[ch] = index_ch
        index_ch += 1

    cipher_list = sorted(cipher)
    text = [[] for _ in range(column)]
    temp = 0
    for i in cipher_list:
        text[cipher[i]].insert(0, mas[temp])
        temp += 1

    message = ""
    for index_text in text:
        message += ''.join(index_text[0])

    return message


if __name__ == '__main__':
    print(UnKeyPermutation("ДВПЕМСЕПРТОЕНОИАГДЬЛЛЮОЬ", 4, 6, "корова"))

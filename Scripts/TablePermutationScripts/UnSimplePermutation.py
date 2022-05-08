def UnSimplePermutation(shifr, row, column):  # Строка - "ПЕСМВДРТЕОПЕИАДГОНЛЮЬОЛЬ"
    shifr = shifr.replace(' ', '').upper()  # Строки - 4, Столбцы - 6 Результат - "ПРИЛЕТАЮСЕДЬМОГОВПОЛДЕНЬ"

    if (len(shifr) != row * column or row <= 0 or column <= 0):
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"

    mas = [[] for _ in range(row)]

    index = -1

    for j in range(row):
        for i in range(column):
            index += 1
            mas[j].insert(i, shifr[index])

    message = ""

    for i in range(column):
        for j in range(row):
            message += mas[j][i]

    return message, mas
def SimplePermutation(message, row, column):  # Шифруемая фраза "Прилетаю седьмого в полдень"
    message = message.replace(' ', '').upper()  # Строки - 4, Столбцы - 6 Результат - "ПЕСМВДРТЕОПЕИАДГОНЛЬЮОЛЬ"
    if (len(message) != row * column or row <= 0 or column <= 0):
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"

    mas = [[] for _ in range(row)]

    index = -1

    for j in range(column):
        for i in range(row):
            index += 1
            mas[i].insert(j, message[index])

    shifr = ""

    for i in range(row):
        for j in range(column):
            shifr += mas[i][j]

    return shifr, mas


if __name__ == '__main__':
    print(SimplePermutation("Прилетаю седьмого в полдень", 4, 6))

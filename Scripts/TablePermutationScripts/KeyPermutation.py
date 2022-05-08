def KeyPermutation(message, row, column, key):
    clear_message = ''.join(message.split(' ')).upper()
    k = row

    if (len(clear_message) != row * column):
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"

    cipher = {}
    index_ch = 0
    for index, ch in enumerate(key.lower()):
        if ch in cipher:
            cipher[ch + str(index_ch)] = clear_message[index * k: index * k + k]
            index_ch += 1
        else:
            cipher[ch] = clear_message[index * k: index * k + k]

    cipher_text = ''.join([''.join([cipher[key][index] for key in sorted(cipher.keys())]) for index in range(k)])

    return cipher_text


if __name__ == '__main__':
    print(KeyPermutation("ПРИЛЕТАЮСЕДЬМОГОВПОЛДЕНЬ", 4, 6, "КОРОВА"))

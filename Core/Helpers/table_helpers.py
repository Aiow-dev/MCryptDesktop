def table_to_str(encrypt_message_table):
    return ''.join('\t'.join(row) + '\n' for row in encrypt_message_table)


def ColumnToRow(mas, row, column):

    index = -1
    newMas = [[] for _ in range(row)]

    for j in range(row):
        for i in range(column):
            index += 1
            newMas[j].insert(i, mas[i][j])

    return newMas


def table_dict_to_str(table_dict):
    return ''.join(key + '\t->\t' + value + '\n-------------------------------------\n'
                   for key, value in table_dict.items())


def tables_to_str(message_table, encrypt_message_table):
    table_dict = {
        message_table[index]: encrypt_message_table[index]
        for index in range(len(message_table))
    }

    return table_dict_to_str(table_dict)
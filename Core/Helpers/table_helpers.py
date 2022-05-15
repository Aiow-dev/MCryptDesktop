def table_to_str(encrypt_message_table):
    return ''.join('\t'.join(row) + '\n' for row in encrypt_message_table)


def ColumnToRow(mas, row, column):
    newMas = [[] for _ in range(row)]

    for j in range(row):
        for i in range(column):
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


def construct_table(columns_values: tuple, table_header: str = None, columns_headers: tuple = None,
                    placeholder: str = '-', len_table_section: int = -1) -> str:
    table = ''

    len_section = len_table_section

    if len_section == -1:
        len_section = len(max(columns_headers, key=len))

    len_table = len_section * len(columns_headers)

    placeholder_line = placeholder * len_table + '\n'

    if table_header:
        table += placeholder_line
        table += f'{f"{table_header}": ^{len_table}}\n'
        table += placeholder_line

    if columns_headers:
        table += f'{f"{columns_headers[0]}": <{len_section}}'

        for index_column_header in range(1, len(columns_headers) - 1):
            table += f'{f"{columns_headers[index_column_header]}": ^{len_section}}'

        table += f'{f"{columns_headers[-1]}": >{len_section}}\n'

    table += placeholder_line

    for index_column_value in range(len(columns_values[0])):
        table += f'{f"{columns_values[0][index_column_value]}": <{len_section}}'

        for index_column in range(1, len(columns_values) - 1):
            table += f'{f"{columns_values[index_column][index_column_value]}": ^{len_section + 3}}'

        table += f'{f"{columns_values[-1][index_column_value]}": >{len_section}}\n'
        index_column_value += 1

    table += placeholder_line

    return table

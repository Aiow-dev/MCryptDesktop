from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QTableWidgetItem


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


def generate_affine_table_number_column(key_a_text, key_b_text, start_t, end_t):
    return [str((key_a_text * t + key_b_text) % 33) for t in range(start_t, end_t)]


def generate_affine_table_column_headers(key_a_text, key_b_text):
    key_text = f'{key_a_text}t+{key_b_text}'

    return 't', key_text, 't', key_text, 't', key_text


def construct_affine_table_number_text(key_a_text, key_b_text):
    column_values = (
        [str(i) for i in range(11)], generate_affine_table_number_column(key_a_text, key_b_text, 0, 11),
        [str(i) for i in range(11, 22)], generate_affine_table_number_column(key_a_text, key_b_text, 11, 22),
        [str(i) for i in range(22, 33)], generate_affine_table_number_column(key_a_text, key_b_text, 22, 33)
    )

    return column_values, construct_table(column_values, columns_headers=generate_affine_table_column_headers(
        key_a_text, key_b_text
    ))


def generate_affine_table_letter_column(number_column_value):
    letters_text = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    return [letters_text[int(number_value)] for number_value in number_column_value]


def construct_affine_table_letter_text(key_a_text, key_b_text, number_column_values):
    column_values = (
        generate_affine_table_letter_column(number_column_values[0]),
        generate_affine_table_letter_column(number_column_values[1]),
        generate_affine_table_letter_column(number_column_values[2]),
        generate_affine_table_letter_column(number_column_values[3]),
        generate_affine_table_letter_column(number_column_values[4]),
        generate_affine_table_letter_column(number_column_values[5])
    )

    return column_values, construct_table(column_values, columns_headers=generate_affine_table_column_headers(
        key_a_text, key_b_text
    ))


def construct_table_column(number_column, column_value, encryption_message_table_obj):
    for number_row, value in enumerate(column_value):
        column_item = QTableWidgetItem(value)
        column_item.setForeground(QBrush(QColor(255, 255, 255)))

        encryption_message_table_obj.setItem(number_row, number_column, column_item)


def construct_affine_table(key_a_text, key_b_text, column_values, encryption_message_table_obj):
    encryption_message_table_obj.setHorizontalHeaderLabels(
        generate_affine_table_column_headers(key_a_text, key_b_text)
    )

    for number_column, column_value in enumerate(column_values):
        construct_table_column(number_column, column_value, encryption_message_table_obj)


def construct_caesar_key_table_text(replace_values):
    column_headers = ('№', '->', '№', '->', '№', '->')

    column_values = (
        generate_affine_table_letter_column([str(i) for i in range(11)]),
        replace_values[:11],
        generate_affine_table_letter_column([str(i) for i in range(11, 22)]),
        replace_values[11:22],
        generate_affine_table_letter_column([str(i) for i in range(22, 33)]),
        replace_values[22:33]
    )

    return column_values, construct_table(column_values, columns_headers=column_headers)


def construct_caesar_key_table(column_values, encryption_message_table_obj):
    column_headers = ('№', '->', '№', '->', '№', '->')

    encryption_message_table_obj.setHorizontalHeaderLabels(column_headers)

    for number_column, column_value in enumerate(column_values):
        construct_table_column(number_column, column_value, encryption_message_table_obj)

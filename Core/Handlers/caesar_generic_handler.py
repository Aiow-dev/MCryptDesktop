from Core.Helpers import table_helpers


def caesar_classic_generic_handler(message_obj, key_obj, encrypt_message_obj,
                                   encryption_message_table_obj, function_caesar_obj):
    try:
        message_text = message_obj.text()
        key_text = int(key_obj.text())

        encrypt_message, message_table, encrypt_message_table = function_caesar_obj(message_text, key_text)
        encrypt_message_obj.setText(encrypt_message)
        encryption_message_table_obj.setText(table_helpers.tables_to_str(message_table, encrypt_message_table))
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
        encryption_message_table_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
    except AttributeError as attribute_error:
        print(attribute_error)


def generate_affine_table_number_column(key_a_text, key_b_text, start_t, end_t):
    return [str((key_a_text * t + key_b_text) % 33) for t in range(start_t, end_t)]


def construct_affine_table_number(key_a_text, key_b_text):
    key_text = f'{key_a_text}t+{key_b_text}'
    column_headers = ('t', key_text, 't', key_text, 't', key_text)

    column_values = (
        [str(i) for i in range(11)], generate_affine_table_number_column(key_a_text, key_b_text, 0, 11),
        [str(i) for i in range(11, 22)], generate_affine_table_number_column(key_a_text, key_b_text, 11, 22),
        [str(i) for i in range(22, 33)], generate_affine_table_number_column(key_a_text, key_b_text, 22, 33)
    )

    return column_values, table_helpers.construct_table(column_values, columns_headers=column_headers)


def generate_affine_table_letter_column(number_column_value):
    letters_text = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    return [letters_text[int(number_value)] for number_value in number_column_value]


def construct_affine_table_letter(key_a_text, key_b_text, number_column_values):
    key_text = f'{key_a_text}t+{key_b_text}'
    column_headers = ('t', key_text, 't', key_text, 't', key_text)

    column_values = (
        generate_affine_table_letter_column(number_column_values[0]),
        generate_affine_table_letter_column(number_column_values[1]),
        generate_affine_table_letter_column(number_column_values[2]),
        generate_affine_table_letter_column(number_column_values[3]),
        generate_affine_table_letter_column(number_column_values[4]),
        generate_affine_table_letter_column(number_column_values[5])
    )

    return table_helpers.construct_table(column_values, columns_headers=column_headers)


def caesar_affine_generic_handler(message_obj, key_a_obj, key_b_obj, encrypt_message_obj,
                                  encryption_message_table_number_obj, encryption_message_table_letter_obj,
                                  function_caesar_obj):
    try:
        message_text = message_obj.text()
        key_a_text = int(key_a_obj.text())
        key_b_text = int(key_b_obj.text())

        encrypt_message, message_table, encrypt_message_table = function_caesar_obj(message_text, key_a_text,
                                                                                    key_b_text)
        encrypt_message_obj.setText(encrypt_message)
        number_column_values, affine_table_number = construct_affine_table_number(key_a_text, key_b_text)
        encryption_message_table_number_obj.setText(affine_table_number)
        encryption_message_table_letter_obj.setText(construct_affine_table_letter(key_a_text, key_b_text,
                                                                                  number_column_values))
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
        encryption_message_table_number_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
        encryption_message_table_letter_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
    except AttributeError as attribute_error:
        print(attribute_error)

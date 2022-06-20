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


def caesar_affine_generic_handler(message_obj, key_a_obj, key_b_obj, encrypt_message_obj,
                                  encryption_message_table_number_text_obj, encryption_message_table_letter_text_obj,
                                  encryption_message_table_number_obj, encryption_message_table_letter_obj,
                                  function_caesar_obj):
    try:
        message_text = message_obj.text()
        key_a_text = int(key_a_obj.text())
        key_b_text = int(key_b_obj.text())

        encrypt_message, message_table, encrypt_message_table = function_caesar_obj(message_text, key_a_text,
                                                                                    key_b_text)
        encrypt_message_obj.setText(encrypt_message)

        number_column_values, affine_table_number = table_helpers.construct_affine_table_number_text(
            key_a_text, key_b_text
        )
        encryption_message_table_number_text_obj.setText(affine_table_number)

        letter_column_values, affine_table_letter = table_helpers.construct_affine_table_letter_text(
            key_a_text, key_b_text, number_column_values
        )
        encryption_message_table_letter_text_obj.setText(affine_table_letter)

        table_helpers.construct_affine_table(
            key_a_text, key_b_text, number_column_values, encryption_message_table_number_obj
        )

        table_helpers.construct_affine_table(
            key_a_text, key_b_text, letter_column_values, encryption_message_table_letter_obj
        )
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
        encryption_message_table_number_text_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
        encryption_message_table_letter_text_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
    except AttributeError as attribute_error:
        print(attribute_error)


def caesar_key_generic_handler(message_obj, key_word_obj, key_k_obj, encrypt_message_obj,
                               encryption_message_table_text_obj, encryption_message_table_obj,
                               function_caesar_obj):
    try:
        message_text = message_obj.text()
        key_word_text = key_word_obj.text().lower()
        key_k_text = int(key_k_obj.text())

        encrypt_message, encrypt_message_table = function_caesar_obj(message_text, key_k_text, key_word_text)
        encrypt_message_obj.setText(encrypt_message)

        letter_column_values, caesar_key_table = table_helpers.construct_caesar_key_table_text(encrypt_message_table)

        encryption_message_table_text_obj.setText(caesar_key_table)

        table_helpers.construct_caesar_key_table(letter_column_values, encryption_message_table_obj)
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
        encryption_message_table_text_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
    except AttributeError as attribute_error:
        print(attribute_error)

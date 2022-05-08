from Core.Helpers import table_helpers


def table_permutation_generic_handler(message_obj, row_obj, column_obj, encrypt_message_obj,
                                      encryption_message_table_obj, function_permutation_obj):
    try:
        message_text = message_obj.text()
        number_row = int(row_obj.text())
        number_column = int(column_obj.text())

        encrypt_message, encrypt_message_table = function_permutation_obj(message_text, number_row,
                                                                          number_column)
        encrypt_message_obj.setText(encrypt_message)
        encryption_message_table_obj.setText(table_helpers.table_to_str(encrypt_message_table))
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
        encryption_message_table_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
    except AttributeError as attribute_error:
        print(attribute_error)


def table_key_permutation_generic_handler(message_obj, row_obj, column_obj, key_obj,
                                          encrypt_message_obj, function_permutation_obj):
    try:
        message_text = message_obj.text()
        number_row = int(row_obj.text())
        number_column = int(column_obj.text())
        key_text = key_obj.text()

        encrypt_message = function_permutation_obj(message_text, number_row,
                                                   number_column, key_text)
        encrypt_message_obj.setText(encrypt_message)
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
    except AttributeError as attribute_error:
        print(attribute_error)
from Scripts.TablePermutationScripts import SimplePermutation
from Scripts.TablePermutationScripts import UnSimplePermutation
from Scripts.TablePermutationScripts import KeyPermutation
from Scripts.TablePermutationScripts import UnKeyPermutation
from Scripts.CaesarScripts import Caesar_Classic
from Scripts.CaesarScripts import UnCaesar_Classic

from Core.Handlers import table_permutation_generic_handler
from Core.Helpers import table_helpers


class HandlersWrapper:
    def __init__(self, ui):
        self.ui = ui

    def simple_permutation_encryption_handler(self):
        table_permutation_generic_handler. \
            table_permutation_generic_handler(self.ui.message_text_smp, self.ui.row_text_smp, self.ui.column_text_smp,
                                              self.ui.encrypt_message_text_smp, self.ui.encryption_table_text_smp,
                                              SimplePermutation.SimplePermutation)

    def un_simple_permutation_encryption_handler(self):
        table_permutation_generic_handler. \
            table_permutation_generic_handler(self.ui.un_message_text_smp, self.ui.un_row_text_smp,
                                              self.ui.un_column_text_smp, self.ui.un_encrypt_message_text_smp,
                                              self.ui.un_encryption_table_text_smp,
                                              UnSimplePermutation.UnSimplePermutation)

    def key_permutation_encryption_handler(self):
        table_permutation_generic_handler. \
            table_key_permutation_generic_handler(self.ui.message_text_kmp, self.ui.row_text_kmp,
                                                  self.ui.column_text_kmp, self.ui.key_text_kmp,
                                                  self.ui.encrypt_message_text_kmp, KeyPermutation.KeyPermutation)

    def un_key_permutation_encryption_handler(self):
        table_permutation_generic_handler. \
            table_key_permutation_generic_handler(self.ui.un_message_text_kmp, self.ui.un_row_text_kmp,
                                                  self.ui.un_column_text_kmp, self.ui.un_key_text_kmp,
                                                  self.ui.un_encrypt_message_text_kmp,
                                                  UnKeyPermutation.UnKeyPermutation)

    def caesar_classic_encryption_handler(self):
        try:
            message_text = self.ui.message_text_sc.text()
            encryption_key = int(self.ui.key_text_sc.text())

            encrypt_message, message_table, encrypt_message_table = Caesar_Classic.Caesar_Classic(message_text,
                                                                                                  encryption_key)

            self.ui.encrypt_message_text_sc.setText(encrypt_message)
            self.ui.encryption_table_text_sc.setText(table_helpers.tables_to_str(message_table, encrypt_message_table))
        except ValueError as value_error:
            print(value_error)

            self.ui.encrypt_message_text_sc.setText('Ошибка. Проверьте корректность введенных данных!')
            self.ui.encryption_table_text_sc.setText(
                'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
            )
        except AttributeError as attribute_error:
            print(attribute_error)

    def un_caesar_classic_encryption_handler(self):
        try:
            message_text = self.ui.un_message_text_sc.text()
            encryption_key = int(self.ui.un_key_text_sc.text())

            un_encrypt_message, message_table, encrypt_message_table = UnCaesar_Classic.UnCaesar_Classic(message_text,
                                                                                                         encryption_key)

            self.ui.un_encrypt_message_text_sc.setText(un_encrypt_message)
            self.ui.un_encryption_table_text_sc.setText(table_helpers.tables_to_str(message_table,
                                                                                    encrypt_message_table))
        except ValueError as value_error:
            print(value_error)

            self.ui.un_message_text_sc.setText('Ошибка. Проверьте корректность введеных данных!')
            self.ui.un_encryption_table_text_sc.setText(
                'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
            )
        except AttributeError as attribute_error:
            print(attribute_error)

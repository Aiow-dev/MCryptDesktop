import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from Interfaces import main_window

from Scripts.TablePermutationScripts import SimplePermutation
from Scripts.TablePermutationScripts import UnSimplePermutation
from Scripts.TablePermutationScripts import KeyPermutation
from Scripts.TablePermutationScripts import UnKeyPermutation
from Scripts.CaesarScripts import Caesar_Classic

from Core.Handlers import table_permutation_generic_handler
from Core.Helpers import table_helpers


def simple_permutation_encryption_handler():
    table_permutation_generic_handler.\
        table_permutation_generic_handler(ui.message_text_smp, ui.row_text_smp, ui.column_text_smp,
                                          ui.encrypt_message_text_smp, ui.encryption_table_text_smp,
                                          SimplePermutation.SimplePermutation)


def un_simple_permutation_encryption_handler():
    table_permutation_generic_handler.\
        table_permutation_generic_handler(ui.un_message_text_smp, ui.un_row_text_smp, ui.un_column_text_smp,
                                          ui.un_encrypt_message_text_smp, ui.un_encryption_table_text_smp,
                                          UnSimplePermutation.UnSimplePermutation)


def key_permutation_encryption_handler():
    table_permutation_generic_handler.\
        table_key_permutation_generic_handler(ui.message_text_kmp, ui.row_text_kmp, ui.column_text_kmp,
                                              ui.key_text_kmp, ui.encrypt_message_text_kmp,
                                              KeyPermutation.KeyPermutation)


def un_key_permutation_encryption_handler():
    table_permutation_generic_handler.\
        table_key_permutation_generic_handler(ui.un_message_text_kmp, ui.un_row_text_kmp, ui.un_column_text_kmp,
                                              ui.un_key_text_kmp, ui.un_encrypt_message_text_kmp,
                                              UnKeyPermutation.UnKeyPermutation)


def caesar_classic_encryption_handler():
    try:
        message_text = ui.message_text_sc.text()
        encryption_key = int(ui.key_text_sc.text())

        encrypt_message, message_table, encrypt_message_table = Caesar_Classic.Caesar_Classic(message_text,
                                                                                              encryption_key)
        ui.encrypt_message_text_sc.setText(encrypt_message)
        ui.encryption_table_text_sc.setText(table_helpers.tables_to_str(message_table, encrypt_message_table))
    except ValueError as value_error:
        print(value_error)

        ui.encrypt_message_text_sc.setText('Ошибка. Проверьте корректность введенных данных!')
        ui.encryption_table_text_sc.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
    except AttributeError as attribute_error:
        print(attribute_error)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.encrypt_btn_smp.clicked.connect(simple_permutation_encryption_handler)
    ui.un_encrypt_btn_smp.clicked.connect(un_simple_permutation_encryption_handler)
    ui.encrypt_btn_kmp.clicked.connect(key_permutation_encryption_handler)
    ui.un_encrypt_btn_kmp.clicked.connect(un_key_permutation_encryption_handler)
    ui.encrypt_btn_sc.clicked.connect(caesar_classic_encryption_handler)

    sys.exit(app.exec_())

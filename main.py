import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from Interfaces import main_window

from Core.Handlers import handlers_wrapper


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    handlers_wrapper = handlers_wrapper.HandlersWrapper(ui)

    ui.encrypt_btn_smp.clicked.connect(handlers_wrapper.simple_permutation_encryption_handler)
    ui.un_encrypt_btn_smp.clicked.connect(handlers_wrapper.un_simple_permutation_encryption_handler)
    ui.encrypt_btn_kmp.clicked.connect(handlers_wrapper.key_permutation_encryption_handler)
    ui.un_encrypt_btn_kmp.clicked.connect(handlers_wrapper.un_key_permutation_encryption_handler)
    ui.encrypt_btn_sc.clicked.connect(handlers_wrapper.caesar_classic_encryption_handler)
    ui.un_encrypt_btn_sc.clicked.connect(handlers_wrapper.un_caesar_classic_encryption_handler)

    sys.exit(app.exec_())

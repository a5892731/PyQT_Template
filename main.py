# author: a5892731
# date: 16.05.2023
# last update: 17.05.2023
# version: 1.0.0
#
# description:
# This is a PyQT GUI application template
#

from sys import argv, exit
from PyQt5.QtWidgets import QApplication

from resources.gui.main_window import MainWindow
from resources.storage.data_storage import DataStorage



if __name__ == "__main__":

    app = QApplication(argv)
    #init data storage
    data_storage = DataStorage()

    #init main graphic window
    main_window = MainWindow(data_storage)
    main_window.show()

    exit(app.exec_())
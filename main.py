import sys


from PyQt5.QtWidgets import QApplication


from resources.gui.main_window import MainWindow
from resources.storage.data_storage import DataStorage





if __name__ == "__main__":

    app = QApplication(sys.argv)
    #init data storage
    data_storage = DataStorage()

    #init main graphic window
    main_window = MainWindow(data_storage)
    main_window.show()

    sys.exit(app.exec_())
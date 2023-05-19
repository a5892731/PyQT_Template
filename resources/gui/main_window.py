from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QFrame

from PyQt5.QtGui import QIcon

from PyQt5.QtCore import QThread, pyqtSignal
import time

class MainWindow(QMainWindow):
    from resources.gui.pages._page1 import page1
    from resources.gui.pages._page2 import page2
    from resources.gui.pages._page3 import page3



    def __init__(self, DataStorage):
        super().__init__()
        self.DataStorage = DataStorage
        self.init_gui()

    def init_gui(self):

        '''window attributes'''
        self.setWindowTitle(self.DataStorage.program_name)
        self.resize(800, 600)  # Set window size
        self.showMaximized()  # Maximized window
        #self.setWindowIcon(QIcon("icon.png"))  # Ustawienie ikony okna

        main_widget = QWidget(self)

        layout = QVBoxLayout(main_widget)

        '''menu'''
        tab_widget = QTabWidget(self)
        layout.addWidget(tab_widget)

        '''here are gui pages'''
        # Page 1 definition in file pages._page1.py
        self.page1(tab_widget)

        # Page 2 definition in file pages._page2.py
        self.page2(tab_widget)

        # Page 3 definition in file pages._page2.py
        self.page3(tab_widget)

        self.setCentralWidget(main_widget)

        '''here are defined backend threads'''
        self.program_thread_1()

    def program_thread_1(self, ):
        self.worker_thread = WorkerThread(self.DataStorage)
        self.worker_thread.signal.connect(self.display_message)

        self.worker_thread.start()

    def display_message(self, message):
        self.DataStorage.test_number += 1
        print(message, self.DataStorage.test_number)

        self.page1_group_box1.entry2.update_number(new_variable=self.DataStorage.test_number)


class WorkerThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, data_storage):
        super().__init__()
        self.data_storage = data_storage

    def run(self):
        while True:
            time.sleep(1)  # Symulacja operacji w tle
            self.signal.emit(self.data_storage.text_data)

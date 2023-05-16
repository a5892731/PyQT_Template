from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QFrame

from PyQt5.QtCore import QThread, pyqtSignal
import time

class MainWindow(QMainWindow):
    from resources.gui.pages._page1 import page1, generate_text
    from resources.gui.pages._page2 import page2
    from resources.gui.pages._page3 import page3



    def __init__(self, data_storage):
        super().__init__()
        self.data_storage = data_storage
        self.init_gui()

    def init_gui(self):

        self.setWindowTitle("Moja aplikacja")

        main_widget = QWidget(self)
        layout = QVBoxLayout(main_widget)

        tab_widget = QTabWidget(self)
        layout.addWidget(tab_widget)

        # Page 1 definition in file pages._page1.py
        self.page1(tab_widget)

        # Page 2 definition in file pages._page2.py
        self.page2(tab_widget)

        # Page 3 definition in file pages._page2.py
        self.page3(tab_widget)

        self.setCentralWidget(main_widget)


        self.program_thread_1()


    def program_thread_1(self, ):
        self.worker_thread = WorkerThread(self.data_storage)
        self.worker_thread.signal.connect(self.display_message)
        self.worker_thread.start()

    def display_message(self, message):
        print(message)


class WorkerThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, data_storage):
        super().__init__()
        self.data_storage = data_storage

    def run(self):
        while True:
            time.sleep(1)  # Symulacja operacji w tle
            self.signal.emit(self.data_storage.text_data)

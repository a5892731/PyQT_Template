from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QWidget

class ListViewExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("List View Example")
        self.setGeometry(100, 100, 400, 300)

        # Tworzenie głównego widgetu
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Tworzenie układu w pionie
        layout = QVBoxLayout(main_widget)

        # Tworzenie listy danych
        data = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

        # Tworzenie modelu danych
        model = QStringListModel()
        model.setStringList(data)

        # Tworzenie QListView
        list_view = QListView()
        list_view.setModel(model)

        # Dodawanie QListView do układu
        layout.addWidget(list_view)

        self.show()

if __name__ == "__main__":
    app = QApplication([])
    window = ListViewExample()
    app.exec_()
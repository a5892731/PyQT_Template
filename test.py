import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout
from PyQt5.QtCore import Qt, QStringListModel


class ListViewExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("List View Example")
        self.setGeometry(100, 100, 400, 300)

        # Create the list view widget
        list_view = QListView(self)
        self.setCentralWidget(list_view)

        # Create and set the model for the list view
        model = QStringListModel()
        model.setStringList(["Item 1", "Item 2", "Item 3"])  # Set the data for the model

        list_view.setModel(model)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ListViewExample()
    sys.exit(app.exec_())
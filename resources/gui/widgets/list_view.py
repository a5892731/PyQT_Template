from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QGroupBox, QLabel, QWidget
from PyQt5.QtCore import Qt, QStringListModel

class ListView(QMainWindow):
    def __init__(self, layout= None, grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True,
                 items = ["Item 1", "Item 2", "Item 3"]):
        super().__init__()
        self.layout = layout

        self.items = items
        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan

    def initUI(self):
        self.setWindowTitle("List View Example")
        self.setGeometry(100, 100, 400, 300)

        # Create the main widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Create a QVBoxLayout to hold the main layout
        #layout = QVBoxLayout(main_widget)

        # Create the list view widget
        list_view = QListView()
        self.layout.addWidget(list_view)

        # Set the model for the list view
        model = QStringListModel()
        model.setStringList(["Item 1", "Item 2", "Item 3"])  # Set the data for the model
        list_view.setModel(model)

        self.show()
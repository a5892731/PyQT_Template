from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QGroupBox, QLabel, QWidget
from PyQt5.QtCore import Qt, QStringListModel, QSize

class ListView(QMainWindow):
    def __init__(self, layout= None, grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True,
                 items = ["Item 1", "Item 2", "Item 3"],
                 DataStorage = None,
                 ):
        super().__init__()
        self.layout = layout

        self.items = items
        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.enable = enable

        self.DataStorage = DataStorage

        self.initUI()

    def initUI(self):
        # Create the list view widget
        self.list_view = QListView()

        #Enable widget
        self.list_view.setEnabled(self.enable)

        # Set the model for the list view
        self.model = QStringListModel()
        self.model.setStringList(self.items)  # Set the data for the model
        self.list_view.setModel(self.model)

        #show widget on layout
        self.layout.addWidget(self.list_view, self.grid_position[0], self.grid_position[1], self.rowspan,
                              self.columnspan)

    def getItems(self):
        string_list = self.model.stringList()
        print(string_list)

    def getSelectedItems(self):
        selected_indexes = self.list_view.selectedIndexes()
        selected_items = [self.model.stringList()[index.row()] for index in selected_indexes]

        if selected_items:
            for item in selected_items:
                print("Selected Item:", item)
        else:
            print("No items selected")

    def addItem(self):
        new_item = "New Item"
        self.model.insertRow(self.model.rowCount())
        self.model.setData(self.model.index(self.model.rowCount() - 1), new_item)
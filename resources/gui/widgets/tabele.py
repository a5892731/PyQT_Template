from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

'''
data example:

        column_names = ["Name", "Age", "Country"]
        
        data_list = [
                    ["John", "25", "USA"],
                    ["Alice", "30", "Canada"],
                    ["Bob", "40", "Australia"],
                    ["Eva", "35", "Germany"]
                    ]

'''



class TableWidget(QWidget):
    def __init__(self, layout = None, column_names = list(), data_list = list(), DataStorage = None,
                 grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True):
        super().__init__()

        self.layout = layout

        self.grid_position = grid_position
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.enable = enable

        self.column_names = column_names
        self.data_list = data_list
        self.DataStorage = DataStorage

        self.initUI()

    def initUI(self):
        self.table = QTableWidget()

        self.table.setColumnCount(len(self.column_names))  # Set the number of columns in the table
        self.table.setRowCount(len(self.data_list))  # Set the number of rows in the table

        self.table.setHorizontalHeaderLabels(self.column_names)  # Set the column header labels


        '''Enable widget'''
        self.table.setEnabled(self.enable)


        for i, row in enumerate(self.data_list):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                self.table.setItem(i, j, item)


        '''show widget on layout'''
        self.layout.addWidget(self.table, self.grid_position[0], self.grid_position[1], self.rowspan,
                              self.columnspan)
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class TableWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        table = QTableWidget()
        table.setColumnCount(3)  # Set the number of columns in the table
        table.setRowCount(4)  # Set the number of rows in the table

        table.setHorizontalHeaderLabels(["Name", "Age", "Country"])  # Set the column header labels

        # Populate the table with data
        data = [
            ["John", "25", "USA"],
            ["Alice", "30", "Canada"],
            ["Bob", "40", "Australia"],
            ["Eva", "35", "Germany"]
        ]

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                table.setItem(i, j, item)

        layout.addWidget(table)

        self.setLayout(layout)
        self.setWindowTitle("Table Widget Example")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWidgetExample()
    sys.exit(app.exec_())
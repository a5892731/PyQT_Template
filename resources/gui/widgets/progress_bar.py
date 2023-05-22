from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt5.QtCore import Qt, QBasicTimer


class ProgressBar(QWidget):
    def __init__(self, layout = None, name = '', DataStorage = None,
                 grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True,):
        super().__init__()

        self.layout = layout
        self.enable = enable
        self.name = name

        self.DataStorage = DataStorage
        self.progress = 0 # Variable to store the current progress

        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.init_ui()

    def init_ui(self):
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(30, 40, 200, 25)  # Set the geometry of the progress bar

        '''Enable widget'''
        self.progressbar.setEnabled(self.enable)

        '''show widget on layout'''
        self.layout.addWidget(self.progressbar, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)

    def set_value(self, progress):
        self.progress = progress
        self.progressbar.setValue(self.progress)  # Set the value of the progress bar



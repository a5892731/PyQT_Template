from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFontDialog, QPushButton
from PyQt5.QtGui import QFont, QColor, QPainter
from PyQt5.QtCore import Qt

class LedRectangle(QWidget):
    def __init__(self, layout=None, on_color = "green", off_color = "red",
                 start_color='grey', dimentions = (40, 20),
                 grid_position = (0, 0), columnspan = 1, rowspan = 1, alignment = Qt.AlignHCenter):
        super().__init__()
        self.layout = layout
        self.start_color = start_color # rgba(0, 0, 0, 0) - transparent
        self.on_color = on_color
        self.off_color = off_color

        self.grid_position = grid_position #grid_layout.addWidget(self.group_box1.group_box, 0, 0)
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.alignment = alignment

        self.width = dimentions[0]
        self.height = dimentions[1]


        self.init_ui()

    def init_ui(self):
        '''create label widget'''
        self.label = QLabel()

        '''dimentions'''
        self.label.setFixedSize(self.width, self.height)

        '''text attributes'''
        self.label.setStyleSheet("background-color: {}".format(self.start_color))


        # Center the label in the window
        #self.label.setAlignment(self.alignment) # AlignHCenter // AlignTop




        '''show widget on layout'''
        self.layout.addWidget(self.label, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)
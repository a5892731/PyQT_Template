from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFontDialog, QPushButton
from PyQt5.QtGui import QFont, QColor, QPainter
from PyQt5.QtCore import Qt

class TextLabelWidget(QWidget):
    def __init__(self, text = 'label', layout=None, font = "Arial", font_size=10, text_color='black',
                 background_color='rgba(0, 0, 0, 0)', text_position = Qt.AlignLeft,
                 grid_position = (0, 0), columnspan = 1, rowspan = 1):
        super().__init__()
        self.text = text
        self.layout = layout
        self.font = font
        self.font_size = font_size
        self.text_color = text_color
        self.background_color = background_color # rgba(0, 0, 0, 0) - transparent
        self.text_position = text_position # AlignLeft; AlignCenter; AlignRight
        self.grid_position = grid_position #grid_layout.addWidget(self.group_box1.group_box, 0, 0)
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.init_ui()

    def init_ui(self):
        '''create label widget'''
        self.label = QLabel(self.text)
        '''text attributes'''
        self.label.setFont(QFont(self.font, self.font_size))
        self.label.setStyleSheet("color: {}; background-color: {}".format(self.text_color, self.background_color))
        self.label.setAlignment(self.text_position)
        '''show widget on layout'''
        #self.layout.addWidget(self.label)
        self.layout.addWidget(self.label, self.grid_position[0], self.grid_position[1], self.columnspan, self.rowspan)
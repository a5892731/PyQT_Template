from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFontDialog, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QColor, QPainter
from PyQt5.QtCore import Qt


class EntryWidget(QWidget):
    def __init__(self, layout=None, font = "Arial", font_size=10, text_color='black',
                 background_color='white', text_position = Qt.AlignLeft,
                 grid_position = (0, 0), columnspan = 1, rowspan = 1,
                 read_only = False):
        super().__init__()
        self.layout = layout
        self.font = font
        self.font_size = font_size
        self.text_color = text_color
        self.background_color = background_color # rgba(0, 0, 0, 0) - transparent
        self.text_position = text_position # AlignLeft; AlignCenter; AlignRight
        self.grid_position = grid_position #grid_layout.addWidget(self.group_box1.group_box, 0, 0)
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.read_only = read_only

        self.init_ui()

    def init_ui(self):
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.on_return_pressed)  # Connect the returnPressed signal to the method


        '''line_edit attributes'''
        self.line_edit.setReadOnly(self.read_only)

        '''show widget on layout'''
        #self.layout.addWidget(self.button)
        self.layout.addWidget(self.line_edit, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)


    def on_return_pressed(self):
        line_edit = self.sender()  # Get the QLineEdit object that triggered the signal
        if line_edit is not None:
            text = line_edit.text()  # Get the entered text
            print("Entered text:", text)

    def write_text(self):
        self.line_edit.setText("")
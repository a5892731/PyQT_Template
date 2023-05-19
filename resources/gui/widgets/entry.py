from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFontDialog, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QColor, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal

'''
use function:

# >>> self.group_box_name.entry_name.update_number(new_variable=variable_to_update)

to update variable in 
'''



class EntryWidget(QWidget):
    def __init__(self, layout=None, font = "Arial", font_size=10, text_color='black',
                 background_color='white', text_position = Qt.AlignLeft,
                 grid_position = (0, 0), columnspan = 1, rowspan = 1,
                 read_only = False, variable=None, output_widget = True):
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
        self.variable = variable
        self.output_widget = output_widget # if True then widget is output, and o False then it is input

        self.read_only = read_only

        self.init_ui()

    def init_ui(self):
        self.line_edit = QLineEdit()
        '''set data'''
        self.line_edit.returnPressed.connect(self.on_return_pressed)  # Connect the returnPressed signal to the method

        if self.output_widget:
            '''line_edit attributes'''
            self.line_edit.setReadOnly(self.read_only)
        else:
            '''print data'''
            self.line_edit.setText(str(self.variable))

        '''show widget on layout'''
        # self.layout.addWidget(self.button)
        self.layout.addWidget(self.line_edit, self.grid_position[0], self.grid_position[1], self.rowspan,
                              self.columnspan)

    def on_return_pressed(self):
        '''get data from entry on enter event'''
        line_edit = self.sender()  # Get the QLineEdit object that triggered the signal
        if line_edit is not None:
            text = line_edit.text()  # Get the entered text
            print("Entered text:", text)

    def update_number(self, new_variable):
        '''update variable in gui function'''
        self.variable = new_variable
        self.line_edit.setText(str(self.variable))
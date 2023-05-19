from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit

'''

TextWidget.set_text(self, text)
'''



class TextWidget(QWidget):
    def __init__(self, layout = None, text = None, read_only = False, output_widget=True,
                 grid_position = (0,0), rowspan = 1, columnspan = 1, size = (400, 300)):
        super().__init__()
        self.layout = layout
        self.text = text

        self.read_only = read_only
        self.output_widget = output_widget # if True then widget is output, and o False then it is input

        self.grid_position = grid_position
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.size = size

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        '''text_edit attributes'''
        self.text_edit.setFixedSize(self.size[0], self.size[1])
        self.text_edit.setReadOnly(self.read_only)

        if self.output_widget:
            self.text_edit.setText(str(self.text))

        '''show widget on layout'''
        self.layout.addWidget(self.text_edit, self.grid_position[0], self.grid_position[1], self.rowspan,
                              self.columnspan)

    def update_text(self, text):
        '''use function to put text on text_widget'''
        self.text_edit.setPlainText(str(text))  # Update the text in QTextEdit

    def add_text(self, text):
        self.text_edit.append(text)  # Add text to QTextEdit

    def clear_text(self):
        '''use function to put text on text_widget'''
        self.text_edit.setPlainText('')  # Clear the text in QTextEdit

    def get_text(self):
        '''use function to get text from text_widget'''
        text_from_widget = self.sender()

        if text_from_widget is not None:
            text = self.text_edit.toPlainText()  # Get text from QTextEdit
            return text
        else:
            return ''
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit


class TextWidget(QWidget):
    def __init__(self, layout = None, read_only = False,
                 grid_position = (0,0), rowspan = 1, columnspan = 1, size = (400, 300)):
        super().__init__()
        self.layout = layout

        self.read_only = read_only

        self.grid_position = grid_position
        self.rowspan = rowspan
        self.columnspan = columnspan
        self.size = size

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.text_edit.setFixedSize(self.size[0], self.size[1])
        self.text_edit.setReadOnly(self.read_only)

        self.text_edit.textChanged.connect(self.on_text_changed)






        '''show widget on layout'''
        self.layout.addWidget(self.text_edit, self.grid_position[0], self.grid_position[1], self.rowspan,
                              self.columnspan)


    def on_text_changed(self):
        self.text_edit = self.sender()
        if self.text_edit is not None:
            text = self.text_edit.toPlainText()  # Get text from QTextEdit
            print("Entered text:", text)

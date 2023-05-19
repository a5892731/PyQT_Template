import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.text_edit = QTextEdit()

        update_button = QPushButton("Update Text")
        update_button.clicked.connect(self.on_update_button_clicked)

        layout.addWidget(self.text_edit)
        layout.addWidget(update_button)

        self.setLayout(layout)
        self.setWindowTitle("QTextEdit Update Text Example")
        self.show()

    def on_update_button_clicked(self):
        new_text = "New text content"
        self.text_edit.setPlainText(new_text)  # Update the text in QTextEdit


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Enter your text:")
        text_edit = QTextEdit()
        text_edit.textChanged.connect(self.on_text_changed)  # Podłączenie sygnału textChanged do metody

        layout.addWidget(label)
        layout.addWidget(text_edit)

        self.setLayout(layout)
        self.setWindowTitle("QTextEdit Example")
        self.show()

    def on_text_changed(self):
        text_edit = self.sender()  # Pobranie obiektu QTextEdit, który wywołał sygnał
        if text_edit is not None:
            text = text_edit.toPlainText()  # Pobranie tekstu z QTextEdit
            print("Entered text:", text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
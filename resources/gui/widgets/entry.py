from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Enter your name:")
        line_edit = QLineEdit()
        line_edit.returnPressed.connect(self.on_return_pressed)  # Podłączenie sygnału returnPressed do metody

        layout.addWidget(label)
        layout.addWidget(line_edit)

        self.setLayout(layout)
        self.setWindowTitle("QLineEdit Example")
        self.show()

    def on_return_pressed(self):
        line_edit = self.sender()  # Pobranie obiektu QLineEdit, który wywołał sygnał
        if line_edit is not None:
            text = line_edit.text()  # Pobranie wprowadzonego tekstu
            print("Entered text:", text)
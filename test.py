from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox, QGridLayout, QLayout, QApplication
from PyQt5.QtCore import Qt
import sys

class ButtonWidget(QWidget):
    def __init__(self, name = 'Click me'):
        super().__init__()
        self.button = None
        self.button_name = name
        self.init_ui()

    def init_ui(self):
        # Create a button
        self.button = QPushButton(self.button_name, self)

        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.button_clicked)

        # show widget
        self.show()

    def button_clicked(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ButtonWidget()
    sys.exit(app.exec_())
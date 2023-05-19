import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Options:")
        checkbox1 = QCheckBox("Option 1")
        checkbox2 = QCheckBox("Option 2")
        checkbox3 = QCheckBox("Option 3")

        # Connect the stateChanged signal to the method
        checkbox1.stateChanged.connect(self.on_checkbox_state_changed)
        checkbox2.stateChanged.connect(self.on_checkbox_state_changed)
        checkbox3.stateChanged.connect(self.on_checkbox_state_changed)

        layout.addWidget(label)
        layout.addWidget(checkbox1)
        layout.addWidget(checkbox2)
        layout.addWidget(checkbox3)

        self.setLayout(layout)
        self.setWindowTitle("QCheckBox Example")
        self.show()

    def on_checkbox_state_changed(self, state):
        checkbox = self.sender()  # Get the QCheckBox object that triggered the signal
        if checkbox is not None:
            option = checkbox.text()  # Get the text from the QCheckBox
            checked = checkbox.isChecked()  # Get the checked state of the QCheckBox
            print("Option:", option)
            print("Checked:", checked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
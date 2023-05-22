from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox

class SpinBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Selected value:")
        self.selected_value_label = QLabel("0")

        spin_box = QSpinBox()
        spin_box.valueChanged.connect(self.updateSelectedValue)

        layout.addWidget(label)
        layout.addWidget(self.selected_value_label)
        layout.addWidget(spin_box)

        self.setLayout(layout)
        self.setWindowTitle("Spin Box Example")
        self.show()

    def updateSelectedValue(self, value):
        self.selected_value_label.setText(str(value))


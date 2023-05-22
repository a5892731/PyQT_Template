import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDoubleSpinBox


class DoubleSpinBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Selected value:")
        self.selected_value_label = QLabel("0.0")

        spin_box = QDoubleSpinBox()
        spin_box.setRange(0.0, 100.0)  # Set the range of the double spin box from 0.0 to 100.0
        spin_box.setSingleStep(0.1)  # Set the step size for incrementing or decrementing the value
        spin_box.setValue(50.0)  # Set the default value of the double spin box to 50.0
        spin_box.valueChanged.connect(self.updateSelectedValue)

        layout.addWidget(label)
        layout.addWidget(self.selected_value_label)
        layout.addWidget(spin_box)

        self.setLayout(layout)
        self.setWindowTitle("Double Spin Box Example")
        self.show()

    def updateSelectedValue(self, value):
        self.selected_value_label.setText(str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DoubleSpinBoxExample()
    sys.exit(app.exec_())
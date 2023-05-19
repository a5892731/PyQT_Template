from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt

class Slider(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Slider Value:")
        slider = QSlider(Qt.Horizontal)

        slider.setMinimum(0)  # Set the minimum value of the slider
        slider.setMaximum(100)  # Set the maximum value of the slider
        slider.setValue(50)  # Set the initial value of the slider

        # Connect the valueChanged signal to the method
        slider.valueChanged.connect(self.on_slider_value_changed)

        layout.addWidget(label)
        layout.addWidget(slider)

        self.setLayout(layout)
        self.setWindowTitle("QSlider Example")
        self.show()

    def on_slider_value_changed(self, value):
        print("Slider value:", value)

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt

class Slider(QWidget):
    def __init__(self, layout = None, name = '', DataStorage = None,
                 min = 0, max = 100, on_start = 50,
                 grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True,):
        super().__init__()

        self.layout = layout
        self.enable = enable
        self.name = name

        self.min = min
        self.max = max
        self.on_start = on_start

        self.DataStorage = DataStorage
        self.value = 0

        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.init_ui()

    def init_ui(self):
        self.slider = QSlider(Qt.Horizontal)

        '''set slider range'''
        self.slider.setMinimum(self.min)  # Set the minimum value of the slider
        self.slider.setMaximum(self.max)  # Set the maximum value of the slider
        self.slider.setValue(self.on_start)  # Set the initial value of the slider

        '''Enable widget'''
        self.slider.setEnabled(self.enable)

        ''' Connect the valueChanged signal to the method '''
        self.slider.valueChanged.connect(self.on_slider_value_changed)

        '''show widget on layout'''
        self.layout.addWidget(self.slider, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)


    def on_slider_value_changed(self, value):
        #print("Slider value:", value)
        self.value = value
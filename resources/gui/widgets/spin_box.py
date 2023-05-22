from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox, QDoubleSpinBox

class SpinBox(QWidget):
    def __init__(self, layout=None, font = "Arial", font_size=10, text_color='black',
                 background_color='white',
                 DataStorage = None, min_value = 0, max_value = 100, floating_point=False, single_step =1,
                 grid_position = (0, 0), columnspan = 1, rowspan = 1,
                 default= 0, read_only = False):

        super().__init__()
        self.layout = layout
        self.font = font
        self.font_size = font_size
        self.text_color = text_color
        self.background_color = background_color # rgba(0, 0, 0, 0) - transparent

        self.grid_position = grid_position #grid_layout.addWidget(self.group_box1.group_box, 0, 0)
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.read_only = read_only # if True then widget is output, and o False then it is input

        self.DataStorage = DataStorage
        self.min_value = min_value
        self.max_value = max_value
        self.floating_point=floating_point
        self.default = default
        self.single_step = single_step



        self.output = None

        self.init_ui()

    def init_ui(self):

        if self.floating_point:
            self.spin_box = QDoubleSpinBox()
        else:
            self.spin_box = QSpinBox()



        '''enable or disable settings'''
        self.spin_box.setReadOnly(self.read_only)
        '''color settings'''
        self.spin_box.setStyleSheet("color: {}; background-color: {}".format(self.text_color, self.background_color))
        '''set range'''
        self.spin_box.setRange(self.min_value, self.max_value)

        '''Set the step size for incrementing or decrementing the value'''
        self.spin_box.setSingleStep(self.single_step)
        '''set default'''
        self.spin_box.setValue(self.default) # change output on change
        '''on change'''
        self.spin_box.valueChanged.connect(self.updateSelectedValue)
        '''show widget on layout'''
        self.layout.addWidget(self.spin_box, self.grid_position[0], self.grid_position[1], self.rowspan,
                              self.columnspan)

    def updateSelectedValue(self, value):
        self.output = value
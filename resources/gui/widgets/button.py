from PyQt5.QtWidgets import QWidget, QPushButton

class ButtonWidget(QWidget):
    def __init__(self, layout= None, name = 'Click me', DataStorage=None, enable=True, on_pressed = True,
                 grid_position = (0, 0), columnspan = 1, rowspan = 1 ):
        super().__init__()
        self.layout = layout
        self.enable = enable
        self.on_pressed = on_pressed
        self.button_name = name
        self.DataStorage = DataStorage
        self.grid_position = grid_position #grid_layout.addWidget(self.group_box1.group_box, 0, 0)
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.init_ui()

    def init_ui(self):
        '''Create a button'''
        self.button = QPushButton(self.button_name, self)

        '''Set button attributes'''
        self.button.setEnabled(self.enable)  # Set button enabled/disabled
        self.button.setCheckable(True)  # Set button as checkable
        self.button.setChecked(False)  # Set initial checked state

        if self.on_pressed:
            '''button operation when pressed'''
            self.button.pressed.connect(self.button_clicked)
        else:
            '''button operation after release'''
            self.button.clicked.connect(self.button_clicked)

        '''show widget on layout'''
        #self.layout.addWidget(self.button)
        self.layout.addWidget(self.button, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)

    def button_clicked(self):
        '''put your button function here'''
        print('Button clicked!')
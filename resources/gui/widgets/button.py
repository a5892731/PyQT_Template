from PyQt5.QtWidgets import QWidget, QPushButton

class ButtonWidget(QWidget):
    def __init__(self, layout= None, name = 'Click me', DataStorage=None, enable=True, on_pressed = True):
        super().__init__()
        self.layout = layout
        self.enable = enable
        self.on_pressed = on_pressed
        self.button_name = name
        self.DataStorage = DataStorage

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
        self.layout.addWidget(self.button)

    def button_clicked(self):
        '''put your button function here'''
        print('Button clicked!')
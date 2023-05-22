from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox

class Checkbox(QWidget):
    def __init__(self, layout = None, name = '', DataStorage = None, set_active = False,
                 grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True,
                 out_when_on = True, out_when_off = False):
        super().__init__()

        self.layout = layout
        self.enable = enable
        self.set_active = set_active
        self.name = name
        self.out_when_on = out_when_on
        self.out_when_off = out_when_off

        self.DataStorage = DataStorage
        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan

        if self.set_active:
            self.output = self.out_when_on
        else:
            self.output = self.out_when_off

        self.init_ui()

    def init_ui(self):

        self.checkbox1 = QCheckBox(self.name)

        '''Connect the stateChanged signal to the method'''
        self.checkbox1.stateChanged.connect(self.on_checkbox_state_changed)

        '''Enable widget'''
        self.checkbox1.setEnabled(self.enable)

        '''show widget on layout'''
        self.layout.addWidget(self.checkbox1, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)


    def on_checkbox_state_changed(self):
        checkbox = self.sender()  # Get the QCheckBox object that triggered the signal
        if checkbox is not None:
            option = checkbox.text()  # Get the text from the QCheckBox
            checked = checkbox.isChecked()  # Get the checked state of the QCheckBox

            if checked:
                self.output = self.out_when_on
            else:
                self.output = self.out_when_off




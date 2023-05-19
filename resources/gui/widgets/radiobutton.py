from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton

class RadioButton(QWidget):
    def __init__(self, layout = None, names_list = list(), output_list = list(), DataStorage = None, set_active = 0,
                 grid_position = (0,0), rowspan = 1, columnspan = 1):
        super().__init__()

        self.layout = layout
        self.enable = True

        self.names_list = names_list
        self.output_list = output_list
        self.set_active = set_active

        self.radiobuttons = []

        self.DataStorage = DataStorage
        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.output = None

        self.init_ui()

    def init_ui(self):

        # create radiobuttons
        for name in self.names_list:
            self.radiobuttons.append(QRadioButton(name))

        # set active on start
        self.radiobuttons[self.set_active].setChecked(True)

        # Connect the toggled signal to the method
        for i in range(len(self.names_list)):
            self.radiobuttons[i].toggled.connect(self.on_radio_button_toggled)

        # add widget
        for i in range(len(self.names_list)):
             self.layout.addWidget(self.radiobuttons[i], self.grid_position[0]+i, self.grid_position[1],
                                  self.rowspan, self.columnspan)


    def on_radio_button_toggled(self):
        radio_button = self.sender()  # Get the QRadioButton object that triggered the signal
        if radio_button is not None and radio_button.isChecked():
            option = radio_button.text()  #  Get the QRadioButton object that triggered the signal

            if len(self.output_list) > 0:
                self.output = self.output_list[self.names_list.index(option)]



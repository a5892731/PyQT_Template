from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox

class MyWidget(QWidget):
    def __init__(self, layout = None, names_list = list(), output_list = list(), DataStorage = None, set_active = 0,
                 grid_position = (0,0), rowspan = 1, columnspan = 1, wertical = True, enable = True):
        super().__init__()

        self.layout = layout
        self.enable = enable

        self.names_list = names_list
        self.output_list = output_list
        self.set_active = set_active

        self.radiobuttons = []

        self.DataStorage = DataStorage
        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.wertical = wertical

        self.output = None

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

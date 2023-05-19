from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class ComboBox(QWidget):
    def __init__(self, layout = None, names_list = list(), output_list = list(), DataStorage = None, set_active = 0,
                 grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True):
        super().__init__()

        self.layout = layout
        self.enable = enable

        self.names_list = names_list
        self.output_list = output_list
        self.set_active = set_active

        self.menu_elements = []

        self.DataStorage = DataStorage
        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan

        if len(self.output_list) > 0:
            self.output = self.output_list[self.set_active]
        else:
            self.output = None

        self.init_ui()

    def init_ui(self):
        self.combo_box = QComboBox()

        # Add items to the combo box
        for name in self.names_list:
            self.combo_box.addItem(name)

        # set enable or disable
        self.combo_box.setEnabled(self.enable)
        # Set the second item as initially selected (index 1)
        self.combo_box.setCurrentIndex(self.set_active)
        # Connect the currentIndexChanged signal to the method
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_index_changed)

        # add widget
        self.layout.addWidget(self.combo_box, self.grid_position[0], self.grid_position[1],
                              self.rowspan, self.columnspan)

    def on_combo_box_index_changed(self):
        combo_box = self.sender()  # Get the QComboBox object that triggered the signal
        if combo_box is not None:
            option = combo_box.currentText()  # Get the currently selected text from the QComboBox

            if len(self.output_list) > 0:
                self.output = self.output_list[self.names_list.index(option)]
            else:
                self.output = None
            #print("Selected option:", option, self.output)

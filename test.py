import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.enable = True

        self.names_list = ["radio1", "radio2", "radio3"]
        self.DataStorage = None
        self.grid_position = (0, 0)
        self.columnspan = 1
        self.rowspan = 1

        self.init_ui()


        self.init_ui()

    def init_ui(self):


        radio_button1 = QRadioButton("Option 1")
        radio_button2 = QRadioButton("Option 2")
        radio_button3 = QRadioButton("Option 3")

        radio_button1.setChecked(True)  # Ustawienie domyślnie zaznaczonego przycisku

        # Połączenie sygnału toggled z metodą
        radio_button1.toggled.connect(self.on_radio_button_toggled)
        radio_button2.toggled.connect(self.on_radio_button_toggled)
        radio_button3.toggled.connect(self.on_radio_button_toggled)


        self.layout.addWidget(radio_button1, self.grid_position[0], self.grid_position[1],
                              self.rowspan, self.columnspan)

        self.layout.addWidget(radio_button2, self.grid_position[1], self.grid_position[1],
                              self.rowspan, self.columnspan)

        self.layout.addWidget(radio_button3, self.grid_position[2], self.grid_position[1],
                              self.rowspan, self.columnspan)


    def on_radio_button_toggled(self):
        radio_button = self.sender()  # Pobranie obiektu QRadioButton, który wywołał sygnał
        if radio_button is not None and radio_button.isChecked():
            option = radio_button.text()  # Pobranie tekstu z QRadioButton
            print("Selected option:", option)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class ComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Select an option:")
        combo_box = QComboBox()

        # Add items to the combo box
        combo_box.addItem("Option 1")
        combo_box.addItem("Option 2")
        combo_box.addItem("Option 3")

        # Connect the currentIndexChanged signal to the method
        combo_box.currentIndexChanged.connect(self.on_combo_box_index_changed)

        layout.addWidget(label)
        layout.addWidget(combo_box)

        self.setLayout(layout)
        self.setWindowTitle("QComboBox Example")
        self.show()

    def on_combo_box_index_changed(self, index):
        combo_box = self.sender()  # Get the QComboBox object that triggered the signal
        if combo_box is not None:
            option = combo_box.currentText()  # Get the currently selected text from the QComboBox
            print("Selected option:", option)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())
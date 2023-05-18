from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt



class GroupBox():
    """this is a parent GroupBox CLASS"""
    def __init__(self, title, page = None, size_x = 200, size_y = 100, DataStorage= None):
        self.page = page
        self.DataStorage = DataStorage
        self.group_box = QGroupBox(title)
        self.group_box.setAlignment(Qt.AlignCenter)
        self.group_box.setFlat(False) # border line
        self.group_box.setMinimumSize(size_x, size_y)  # Set minimal size

        self.layout = QVBoxLayout()

        self.define_widgets()

        self.group_box.setLayout(self.layout)
        #widgets positioning
        self.group_box.setAlignment(Qt.AlignTop)
        self.group_box.setAlignment(Qt.AlignLeft)

    def define_widgets(self):
        """This function need to be filed in child class with widgets"""
        pass




from PyQt5.QtWidgets import QFrame, QGroupBox, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt



class GroupBox():
    """this is a parent GroupBox CLASS"""
    def __init__(self, title, page = None, size_x = 200, size_y = 100):
        self.page = page
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


    def import_data(self, DataStorage):
        '''If group box will use program data from stora_data.py use this function to connect to DataStorage class'''
        self.DataStorage = DataStorage

    def define_widgets(self):
        """This function need to be filed in child class with widgets

        self.button = ButtonWidget(layout=self.layout)
        """
        pass




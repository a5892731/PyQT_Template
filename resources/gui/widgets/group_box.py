from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QGridLayout, QWidget, QLayout
from PyQt5.QtCore import Qt

'''
Warning!
Group Box must be included as self.group_box_name if you want to use any buttons inside it.
'''


class GroupBox(QWidget):
    """this is a parent GroupBox CLASS"""
    def __init__(self, title, grid_layout = None, size_x = 200, size_y = 100, DataStorage= None,
                 grid_position = (0, 0), columnspan = 1, rowspan = 1, alignment=Qt.AlignTop):
        super().__init__()
        '''data'''
        self.paste_on_grid = grid_layout
        self.DataStorage = DataStorage
        '''layouts'''
        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        '''create group box'''
        self.group_box = QGroupBox(title)
        '''group box attributes'''

        self.group_box.setFlat(False)  # border line
        self.group_box.setMinimumSize(size_x, size_y)  # Set minimal size
        ''' widgets positioning'''
        self.grid_layout.setAlignment(alignment)
        #self.group_box.setAlignment(Qt.AlignCenter)
        #self.grid_layout.setAlignment(Qt.AlignLeft)
        '''call your widgets'''
        self.define_widgets()
        '''grid settings'''
        self.group_box.setLayout(self.grid_layout)
        self.layout.addWidget(self.group_box)
        self.setLayout(self.layout)  # Set layout

        '''paste group box on grid'''
        self.paste_on_grid.addWidget(self.group_box, grid_position[0], grid_position[1], rowspan, columnspan)

    def define_widgets(self):
        """This function need to be filed in child class with widgets"""
        pass



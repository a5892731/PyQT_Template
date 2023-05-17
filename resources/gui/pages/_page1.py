from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox, QGridLayout, QLayout
from PyQt5.QtCore import Qt

from resources.gui.widgets.group_box_class import GroupBox



def page1(self, tab_widget):
    '''page 1 atrubutes'''
    page1 = QWidget(self)
    grid_layout = QGridLayout(page1)

    '''define widgets'''
    group_box1 = GroupBox1(title="title", page=grid_layout)
    group_box1.import_data(DataStorage = self.data_storage)
    group_box2 = GroupBox1(title="title")

    '''add widgets to layout grid'''
    grid_layout.addWidget(group_box1.group_box, 0, 0)
    grid_layout.addWidget(group_box2.group_box, 0, 1)

    '''grid settings'''
    grid_layout.setRowStretch(0, 0)  # Restrict row 0
    grid_layout.setColumnStretch(0, 0)  # Restrict column 0
    grid_layout.setSizeConstraint(QLayout.SetFixedSize)        # Set size constraint
    self.setLayout(grid_layout)         # Set layout

    '''end page 1'''
    tab_widget.addTab(page1, "Page 1")


class GroupBox1(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets

        self.button = ButtonWidget(layout=self.layout)
        """
        self.button = ButtonWidget(layout=self.layout)




class ButtonWidget(QWidget):
    def __init__(self, name = 'Click me', layout=None):
        super().__init__()
        self.button = None
        self.button_name = name
        self.layout = layout
        self.init_ui()

    def init_ui(self):
        # Create a button
        self.button = QPushButton(self.button_name, self)

        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.button_clicked)

        # show widget
        self.show()

        self.layout.addWidget(self.button)

    def button_clicked(self):
        print('Button clicked!')
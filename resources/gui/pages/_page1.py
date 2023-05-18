from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox, QGridLayout, QLayout
from PyQt5.QtCore import Qt

from resources.gui.widgets.group_box import GroupBox
from resources.gui.widgets.button import ButtonWidget
from resources.gui.widgets.text_label import TextLabelWidget


def page1(self, tab_widget):
    '''page 1 atrubutes'''
    page1 = QWidget(self)
    grid_layout = QGridLayout(page1)

    '''define widgets'''
    self.group_box1 = GroupBox1(title="title", grid_layout=grid_layout, DataStorage=self.DataStorage)

    '''add widgets to layout grid'''
    grid_layout.addWidget(self.group_box1.group_box, 0, 0)

    '''grid settings'''
    grid_layout.setRowStretch(0, 0)  # Restrict row 0
    grid_layout.setColumnStretch(0, 0)  # Restrict column 0
    grid_layout.setSizeConstraint(QLayout.SetFixedSize)        # Set size constraint
    self.setLayout(grid_layout)         # Set layout

    '''end page 1'''
    tab_widget.addTab(page1, "Page 1")


class GroupBox1(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""
        self.button = Button(layout=self.grid_layout, name = "button", DataStorage=self.DataStorage, grid_position=(0, 0))
        self.label = TextLabelWidget(text = 'label ..........:', layout=self.grid_layout,
                                     font = "Arial", font_size=10, grid_position=(1, 0))

class Button(ButtonWidget):
    def button_clicked(self):
        '''put your button function here'''
        self.DataStorage.text_data = "new text"
        print('Button clicked!')

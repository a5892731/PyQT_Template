from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox, QGridLayout, QLayout
from PyQt5.QtCore import Qt

from resources.gui.widgets.group_box import GroupBox
from resources.gui.widgets.button import ButtonWidget
from resources.gui.widgets.text_label import TextLabelWidget


def page2(self, tab_widget):
    '''page 2 atrubutes'''
    page2 = QWidget(self)
    grid_layout = QGridLayout(page2)

    '''define widgets'''
    self.page2_group_box1 = Page2_GroupBox1(title="title", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 0), columnspan = 0, rowspan = 2 )
    self.page2_group_box2 = Page2_GroupBox1(title="title", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (20, 0), columnspan = 1, rowspan = 1 )

    self.page2_group_box3 = Page2_GroupBox1(title="title", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (20, 1), columnspan = 1, rowspan = 1 )

    '''grid settings'''
    grid_layout.setRowStretch(0, 0)  # Restrict row 0
    grid_layout.setColumnStretch(0, 0)  # Restrict column 0
    grid_layout.setSizeConstraint(QLayout.SetFixedSize)        # Set size constraint
    self.setLayout(grid_layout)         # Set layout

    '''end page 1'''
    tab_widget.addTab(page2, "Page 2")


class Page2_GroupBox1(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""
        self.page2_button1 = Page2_Button1(layout=self.grid_layout, name = "button", DataStorage=self.DataStorage,
                                    grid_position=(0, 0))

        self.page2_label1 = TextLabelWidget(text = 'label:', layout=self.grid_layout,
                                     font = "Arial", font_size=10, grid_position=(1, 0))

class Page2_Button1(ButtonWidget):
    def button_clicked(self):
        '''put your button function here'''
        self.DataStorage.text_data = "new text 2"
        print('Button clicked!')

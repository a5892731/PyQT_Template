from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox, QGridLayout, QLayout
from PyQt5.QtCore import Qt

from resources.gui.widgets.group_box import GroupBox
from resources.gui.widgets.button import ButtonWidget
from resources.gui.widgets.text_label import TextLabelWidget
from resources.gui.widgets.entry import EntryWidget


def page1(self, tab_widget):
    '''page 1 atrubutes'''
    page1 = QWidget(self)
    grid_layout = QGridLayout(page1)

    '''define widgets'''
    self.page1_group_box1 = Page1_GroupBox1(title="title", grid_layout=grid_layout, DataStorage=self.DataStorage)

    '''grid settings'''
    grid_layout.setRowStretch(0, 0)  # Restrict row 0
    grid_layout.setColumnStretch(0, 0)  # Restrict column 0
    grid_layout.setSizeConstraint(QLayout.SetFixedSize)        # Set size constraint
    self.setLayout(grid_layout)         # Set layout

    '''end page 1'''
    tab_widget.addTab(page1, "Page 1")


class Page1_GroupBox1(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""
        self.button = Page1_Button(layout=self.grid_layout, name = "button", DataStorage=self.DataStorage, grid_position=(0, 0))
        self.label = TextLabelWidget(text = 'label ..........:', layout=self.grid_layout,
                                     font = "Arial", font_size=10, grid_position=(1, 0))

        self.entry = EntryWidget(layout=self.grid_layout, font = "Arial", font_size=10, text_color='black',
                 background_color='white', text_position = Qt.AlignLeft,
                 grid_position = (2, 0))

        self.entry2 = EntryWidget(layout=self.grid_layout, font = "Arial", font_size=10, text_color='black',
                 background_color='white', text_position = Qt.AlignLeft, read_only = True,
                 grid_position = (3, 0))


class Page1_Button(ButtonWidget):
    def button_clicked(self):
        '''put your button function here'''
        self.DataStorage.text_data = "new text"
        print('Button clicked!')

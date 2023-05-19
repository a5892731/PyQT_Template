from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox, QGridLayout, QLayout
from PyQt5.QtCore import Qt

from resources.gui.widgets.group_box import GroupBox
from resources.gui.widgets.button import ButtonWidget
from resources.gui.widgets.text_label import TextLabelWidget
from resources.gui.widgets.entry import EntryWidget
from resources.gui.widgets.text_widget import TextWidget
from resources.gui.widgets.radiobutton import RadioButton
from resources.gui.widgets.checkbox import Checkbox
from resources.gui.widgets.combobox import ComboBox


def page1(self, tab_widget):
    '''page 1 atrubutes'''
    page1 = QWidget(self)
    grid_layout = QGridLayout(page1)

    '''define widgets'''
    self.page1_group_box1 = Page1_GroupBox1(title="title", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 0))

    self.page1_group_box2 = Page1_GroupBox1(title="title2", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 1))

    self.page1_group_box3 = Page1_GroupBox3(title="title3", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (1, 0), columnspan=2)

    self.page1_group_box4 = Page1_GroupBox4(title="title4", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 3), columnspan=1)

    self.page1_group_box5 = Page1_GroupBox5(title="title4", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 4), columnspan=1)



    '''grid settings'''
    #grid_layout.setRowStretch(0, 0)  # Restrict row 0
    #grid_layout.setColumnStretch(0, 0)  # Restrict column 0
    grid_layout.setSizeConstraint(QLayout.SetFixedSize)        # Set size constraint
    self.setLayout(grid_layout)         # Set layout

    '''end page 1'''
    tab_widget.addTab(page1, "Page 1")

'''------------------------------------------------------------------------------------------------------------------'''

class Page1_GroupBox1(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""
        self.button = Page1_Button(layout=self.grid_layout, name = "button", DataStorage=self.DataStorage,
                                   grid_position=(0, 0), columnspan=2)
        self.label = TextLabelWidget(text = 'input: ', layout=self.grid_layout,
                                     font = "Arial", font_size=10, grid_position=(1, 0))

        self.entry = EntryWidget(layout=self.grid_layout, font = "Arial", font_size=10, text_color='black',
                 background_color='white', text_position = Qt.AlignLeft,
                 grid_position = (1, 1), read_only = False, default='', output_widget = False)


        self.label = TextLabelWidget(text = 'output: ', layout=self.grid_layout,
                                     font = "Arial", font_size=10, grid_position=(2, 0))

        self.entry2 = EntryWidget(layout=self.grid_layout, font = "Arial", font_size=10, text_color='black',
                 background_color='white', text_position = Qt.AlignLeft,
                 grid_position = (2, 1), read_only = True, default='default', output_widget = True)


class Page1_GroupBox3(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""
        self.text = TextWidget(layout = self.grid_layout, grid_position = (0,0), rowspan = 1, columnspan = 1,
                               size = (200, 300),
                               read_only = False, output_widget=False)

        self.text2 = TextWidget(layout = self.grid_layout, grid_position = (0,1), rowspan = 1, columnspan = 1,
                                size = (200, 300),
                                read_only = True, output_widget=True)

        self.button2 = Page1_Button2(layout=self.grid_layout, name = "wyślij", DataStorage=self,
                                     grid_position=(2, 0), columnspan=2)


        self.button3 = Page1_Button3(layout=self.grid_layout, name = "dodaj", DataStorage=self,
                                     grid_position=(3, 0), columnspan=2)



class Page1_GroupBox4(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""


        names_list = ['radiobutton1', 'radiobutton2', 'radiobutton3']
        output_list = ['out1', 'out2', 'out3']

        self.radiobutton = RadioButton(layout = self.grid_layout, names_list = names_list, output_list = output_list,
                                       DataStorage = None, set_active = 0, enable = True,
                                       grid_position = (0,0), rowspan = 1, columnspan = 1, wertical = True)


        self.checkbox1 = Checkbox(layout = self.grid_layout, name = 'check1', DataStorage = None, set_active = False,
                                  grid_position = (4,0), rowspan = 1, columnspan = 1, enable = True,
                                  out_when_on = True, out_when_off = False)


class Page1_GroupBox5(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        names_list = ['option1', 'option2', 'option3']
        output_list = ['out1', 'out2', 'out3']

        self.combobox = ComboBox(layout = self.grid_layout, names_list = names_list, output_list = output_list,
                                 DataStorage = None, set_active = 1,
                                 grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True)
'''------------------------------------------------------------------------------------------------------------------'''

class Page1_Button(ButtonWidget):
    def button_clicked(self):
        '''put your button function here'''
        self.DataStorage.text_data = "new text"
        print('Button clicked!')

class Page1_Button2(ButtonWidget):
    def button_clicked(self):
        '''put your button function here'''
        self.DataStorage.DataStorage.text_data = self.DataStorage.text.get_text()

        self.DataStorage.text2.update_text(self.DataStorage.DataStorage.text_data) # DataStorage of button.group_box
        print('wyślij button clicked!')

class Page1_Button3(ButtonWidget):
    def button_clicked(self):
        '''put your button function here'''
        self.DataStorage.DataStorage.text_data = self.DataStorage.text.get_text()

        self.DataStorage.text2.add_text(self.DataStorage.DataStorage.text_data) # DataStorage of button.group_box
        print('wyślij button clicked!')
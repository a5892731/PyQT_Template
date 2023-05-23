from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox, QGridLayout, QLayout
from PyQt5.QtCore import Qt

from resources.gui.widgets._widgets_lib import GroupBox, ButtonWidget, TextLabelWidget, EntryWidget, TextWidget, \
    RadioButton, Checkbox, ComboBox, Slider, ProgressBar, SpinBox, CalendarWidget, TableWidget, TreeView, ListView, \
    LabelImage


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

    self.page1_group_box6 = Page1_GroupBox6(title="title5", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 5), columnspan=1)

    self.page1_group_box7 = Page1_GroupBox7(title="title6", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 6), columnspan=1)

    self.page1_group_box8 = Page1_GroupBox8(title="title7", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 7), columnspan=1)

    self.page1_group_box9 = Page1_GroupBox9(title="title8", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (2, 0), columnspan=2)

    self.page1_group_box10 = Page1_GroupBox10(title="title9", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (1, 3), columnspan=2)


    self.page1_group_box11 = Page1_GroupBox11(title="title10", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (1, 5), columnspan=1)


    self.page1_group_box12 = Page1_GroupBox12(title="title11", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (1, 6), columnspan=1)




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


class Page1_GroupBox6(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        self.slider = Slider(layout = self.grid_layout, name = 'slider',
                             DataStorage = None,
                             min = 0, max = 100, on_start = 50,
                             grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True,)


        self.entry = EntryWidget(layout=self.grid_layout, font = "Arial", font_size=10, text_color='black',
                 background_color='white', text_position = Qt.AlignLeft,
                 grid_position = (2, 0), read_only = True, default='', output_widget = True)

class Page1_GroupBox7(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        self.progressbar = ProgressBar(layout = self.grid_layout, name = '', DataStorage = None,
                                       grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True,)

        self.progressbar.set_value(progress=50)


class Page1_GroupBox8(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        self.spinbox = SpinBox(layout=self.grid_layout, font = "Arial", font_size=10, text_color='black',
                 background_color='white',
                 DataStorage = None, min_value = 0.0, max_value = 1010.0, floating_point=True, single_step =1.0,
                 grid_position = (0, 0), columnspan = 1, rowspan = 1,
                 default= 0.0, read_only = False)

class Page1_GroupBox9(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        self.calendar = CalendarWidget(layout=self.grid_layout)


class Page1_GroupBox10(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        column_names = ["Name", "Age", "Country"]

        data_list = [
            ["John", "25", "USA"],
            ["Alice", "30", "Canada"],
            ["Bob", "40", "Australia"],
            ["Eva", "35", "Germany"]
        ]

        self.table = TableWidget(layout=self.grid_layout, column_names = column_names, data_list = data_list,
                                 DataStorage = None,
                                 grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True)


class Page1_GroupBox11(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        items = ["Item 1", "Item 2", "Item 3"]

        self.list_view = ListView(layout=self.grid_layout, grid_position = (0,0), rowspan = 1, columnspan = 1,
                                  enable = True, items = items, DataStorage = self.DataStorage)


        self.button = Page1_Button4(layout=self.grid_layout, name = "get item", DataStorage=self,
                                   grid_position=(1, 0), columnspan=1)


class Page1_GroupBox12(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        self.image = LabelImage(layout = self.grid_layout, max_side_size = 120,
                                image_address = "resources/gui/graphics/example.jpg",
                                grid_position = (0, 0), columnspan = 1, rowspan = 1, rotate= 45)

        #self.grid_layout.setContentsMargins(0, 0, 0, 0)
        #self.grid_layout.setAlignment(Qt.AlignTop)


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

class Page1_Button4(ButtonWidget):
    def button_clicked(self):
        '''put your button function here'''
        self.DataStorage.list_view.getItems()

        self.DataStorage.list_view.getSelectedItems()

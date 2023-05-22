from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox, QGridLayout, QLayout
from PyQt5.QtCore import Qt

from resources.gui.widgets._widgets_lib import GroupBox, ButtonWidget, TextLabelWidget, EntryWidget, TextWidget, \
    RadioButton, Checkbox, ComboBox, Slider, ProgressBar, SpinBox, CalendarWidget, TableWidget, TreeView


def page3(self, tab_widget):
    '''page 1 atrubutes'''
    page1 = QWidget(self)
    grid_layout = QGridLayout(page1)



    '''define widgets'''


    self.page3_group_box10 = Page3_GroupBox1(title="title9", grid_layout=grid_layout, DataStorage=self.DataStorage,
                                            grid_position = (0, 0), columnspan=2)

    '''grid settings'''
    #grid_layout.setRowStretch(0, 0)  # Restrict row 0
    #grid_layout.setColumnStretch(0, 0)  # Restrict column 0
    grid_layout.setSizeConstraint(QLayout.SetFixedSize)        # Set size constraint
    self.setLayout(grid_layout)         # Set layout

    '''end page 1'''
    tab_widget.addTab(page1, "Page 3")

'''------------------------------------------------------------------------------------------------------------------'''


class Page3_GroupBox1(GroupBox):
    def define_widgets(self):
        """This function need to be filed in child class with widgets"""

        self.tree = TreeView(layout=self.grid_layout)





'''------------------------------------------------------------------------------------------------------------------'''


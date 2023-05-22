import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate


class CalendarWidget(QWidget):
    def __init__(self, layout, grid_position = (0,0), rowspan = 1, columnspan = 1,):
        super().__init__()
        self.layout = layout

        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.initUI()

    def initUI(self):


        label = QLabel("Selected date:")
        self.selected_date_label = QLabel()

        self.calendar = QCalendarWidget()  # Prefix 'self' to make 'calendar' an instance variable
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.updateSelectedDate)

        default_date = QDate.currentDate()
        self.calendar.setSelectedDate(default_date)  # Use 'self.calendar' to refer to the instance variable
        self.updateSelectedDate()



        '''show widget on layout'''
        self.layout.addWidget(label, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)
        self.layout.addWidget(self.selected_date_label, self.grid_position[0]+1, self.grid_position[1], self.rowspan, self.columnspan)
        self.layout.addWidget(self.calendar, self.grid_position[0]+2, self.grid_position[1], self.rowspan, self.columnspan)


    def updateSelectedDate(self):
        selected_date = self.calendar.selectedDate()  # Use 'self.calendar' to refer to the instance variable
        self.selected_date_label.setText(selected_date.toString("yyyy-MM-dd"))



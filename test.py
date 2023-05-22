import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate


class CalendarWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Selected date:")
        self.selected_date_label = QLabel()

        self.calendar = QCalendarWidget()  # Prefix 'self' to make 'calendar' an instance variable
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.updateSelectedDate)

        default_date = QDate.currentDate()
        self.calendar.setSelectedDate(default_date)  # Use 'self.calendar' to refer to the instance variable
        self.updateSelectedDate()

        layout.addWidget(label)
        layout.addWidget(self.selected_date_label)
        layout.addWidget(self.calendar)  # Use 'self.calendar' to refer to the instance variable

        self.setLayout(layout)
        self.setWindowTitle("Calendar Widget Example")
        self.show()

    def updateSelectedDate(self):
        selected_date = self.calendar.selectedDate()  # Use 'self.calendar' to refer to the instance variable
        self.selected_date_label.setText(selected_date.toString("yyyy-MM-dd"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarWidgetExample()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QFrame

def page2(self, tab_widget):
    page2 = QWidget(self)
    layout_page2 = QVBoxLayout(page2)
    checkbox1 = QCheckBox("Opcja 1", self)
    checkbox2 = QCheckBox("Opcja 2", self)
    layout_page2.addWidget(checkbox1)
    layout_page2.addWidget(checkbox2)
    tab_widget.addTab(page2, "Page 2")
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QFrame

def page1(self, tab_widget):
    page1 = QWidget(self)
    layout_page1 = QVBoxLayout(page1)
    button = QPushButton("Generuj", self)
    button.clicked.connect(self.generate_text)
    text_box = QLineEdit(self)
    layout_page1.addWidget(button)
    layout_page1.addWidget(text_box)
    tab_widget.addTab(page1, "Page 1")

def generate_text(self):
    self.data_storage.text_data = "Udało się!"
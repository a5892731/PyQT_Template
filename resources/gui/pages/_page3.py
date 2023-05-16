from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QFrame

def page3(self, tab_widget):
    page3 = QWidget(self)
    layout_page3 = QVBoxLayout(page3)
    label_frame = QFrame(self)
    label_frame.setFrameShape(QFrame.Box)
    label_frame_layout = QVBoxLayout(label_frame)
    label = QLabel("Napis w środku", self)
    # label.setAlignment(Qt.AlignCenter)
    label_frame_layout.addWidget(label)
    layout_page3.addWidget(label_frame)
    tab_widget.addTab(page3, "Page 3")
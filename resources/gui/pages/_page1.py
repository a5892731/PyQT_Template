from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTabWidget, \
    QCheckBox, QLabel, QGroupBox

from PyQt5.QtCore import Qt  # Dodanie importu modułu QtCore

def page1(self, tab_widget):
    def label_frame(title):
        def widgets_in_labelframe(layout):
            '''
            Add your widgets here
            '''
            button = QPushButton("Kliknij mnie")
            layout.addWidget(button)

        group_box = QGroupBox(title)
        #group_box.setAlignment(Qt.AlignCenter)
        group_box.setFlat(False)
        group_box.setMinimumSize(200, 100)  # Set minimal size
        group_box.setMaximumSize(200, 100)  # Set maximal size

        layout = QVBoxLayout()


        widgets_in_labelframe(layout)  # widgets inside

        group_box.setLayout(layout)

        return group_box

    '''page 1 atrubutes'''
    page1 = QWidget(self)
    layout_page1 = QVBoxLayout(page1)

    '''define widgets'''
    label_frame = label_frame("tekst")


    '''add widgets'''
    layout_page1.addWidget(label_frame)
    layout_page1.setAlignment(label_frame, Qt.AlignTop | Qt.AlignLeft)  # Ustawienie wyrównania widgetu
    '''end page 1'''
    tab_widget.addTab(page1, "Page 1")



def generate_text(self):
    self.data_storage.text_data = "Udało się!"


from PyQt5.QtWidgets import QFrame,


def label_frame(title):
    def widgets_in_labelframe(layout):
        '''
        Add your widgets here
        '''
        button = QPushButton("Kliknij mnie")
        layout.addWidget(button)


    group_box = QGroupBox(title)
    group_box.setAlignment(Qt.AlignCenter)
    group_box.setFlat(False)
    group_box.setMinimumSize(200, 100)  # Set minimal size

    layout = QVBoxLayout()


    widgets_in_labelframe(layout) # widgets inside

    group_box.setLayout(layout)

    return layout
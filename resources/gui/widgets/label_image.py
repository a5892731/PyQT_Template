from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
'''
warning:
use 
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setAlignment(Qt.AlignTop)
in your grid settings

'''

class LabelImage(QWidget):
    def __init__(self,  layout = None, max_side_size = 180, image_address = "resources/gui/graphics/example.jpg",
                 grid_position = (0, 0), columnspan = 1, rowspan = 1):
        super().__init__()

        self.layout = layout

        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan

        self.max_side_size = max_side_size

        self.image_address = image_address

        self.initUI()

    def initUI(self):
        # Create a label to display the image
        self.label = QLabel(self)

        # Load the image using QPixmap
        self.pixmap = QPixmap(self.image_address)

        # Scale the pixmap to the desired size
        self.scaled_pixmap = self.resize_image(self.max_side_size)

        # Set the scaled pixmap as the content of the label
        self.label.setPixmap(self.scaled_pixmap)

        # Center the label in the window
        self.label.move(0, 0)
        self.label.setContentsMargins(0, 0, 0, 0)
        self.label.setAlignment(Qt.AlignTop)

        #show widget on layout
        self.layout.addWidget(self.label, self.grid_position[0], self.grid_position[1], self.rowspan,
                             self.columnspan)

    def resize_image(self, max_side_size):
        image_size  = self.pixmap.size()
        width = image_size.width()
        height = image_size.height()

        '''function is resizing image by his longest side to "max_side_size"
        other side is proportional to original'''

        if height > width:
            scale = height / max_side_size
            width = width / scale
            height = height / scale
        else:
            scale = width / max_side_size
            width = width / scale
            height = height / scale

        new_width = int(width)
        new_height = int(height)

        return self.pixmap.scaled(new_width, new_height)  # Change the size here


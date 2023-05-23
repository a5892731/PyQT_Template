from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap

class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.max_side_size = 200

        self.initUI()

    def initUI(self):
        # Create a label to display the image
        label = QLabel(self)

        # Load the image using QPixmap
        self.pixmap = QPixmap("resources/gui/graphics/example.jpg")

        # Scale the pixmap to the desired size
        self.scaled_pixmap = self.resize_image(self.max_side_size)

        # Set the scaled pixmap as the content of the label
        label.setPixmap(self.scaled_pixmap)


        # Center the label in the window
        #label.move(self.width() // 2 - scaled_pixmap.width() // 2, self.height() // 2 - scaled_pixmap.height() // 2)

        self.setWindowTitle("Image Widget")
        self.setGeometry(100, 100, 400, 300)
        self.show()

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



if __name__ == '__main__':
    app = QApplication([])
    window = ImageWidget()
    app.exec_()
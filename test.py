from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QBitmap
from PyQt5.QtCore import Qt

class RoundImage(QWidget):
    def __init__(self, layout=None, image_address="resources/gui/graphics/example.jpg",
                 grid_position=(0, 0), columnspan=1, rowspan=1):
        super().__init__()

        self.layout = layout

        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.image_address = image_address

        self.initUI()

    def initUI(self):
        # Create a label to display the image
        self.label = QLabel(self)

        # Load the image using QPixmap
        self.pixmap = QPixmap(self.image_address)

        # Set the label size to match the pixmap size
        self.label.setFixedSize(self.pixmap.size())

        # Create a circular mask
        mask = QBitmap(self.pixmap.size())
        mask.fill(Qt.color0)

        painter = QPainter(mask)
        painter.setBrush(Qt.color1)
        painter.setRenderHint(QPainter.Antialiasing)

        # Calculate the center and radius of the circle
        center = self.pixmap.rect().center()
        radius = min(center.x(), center.y())

        # Draw the circular mask
        painter.drawEllipse(center, radius, radius)

        painter.end()

        # Apply the mask to the pixmap
        self.pixmap.setMask(mask)

        # Set the pixmap as the content of the label
        self.label.setPixmap(self.pixmap)

        # Show widget on layout
        self.layout.addWidget(self.label, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)


# Example usage
app = QApplication([])
window = QWidget()

layout = QVBoxLayout(window)

round_image = RoundImage(layout=layout, image_address="resources/gui/graphics/example.jpg")

window.setLayout(layout)
window.show()

app.exec_()

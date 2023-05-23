from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PyQt5.QtGui import QFont, QTransform
from PyQt5.QtCore import Qt

app = QApplication([])
view = QGraphicsView()
scene = QGraphicsScene()

label1 = QGraphicsTextItem("Label 1")
label1.setFont(QFont("Arial", 12))
label1.setTransformOriginPoint(label1.boundingRect().center())
label1.setRotation(45)  # Obrót o 45 stopni

label2 = QGraphicsTextItem("Label 2")
label2.setFont(QFont("Arial", 12))
label2.setTransformOriginPoint(label2.boundingRect().center())
label2.setRotation(-30)  # Obrót o -30 stopni

scene.addItem(label1)
scene.addItem(label2)

view.setScene(scene)
view.show()

app.exec_()

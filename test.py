import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt5.QtCore import Qt, QBasicTimer


class ProgressBarExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(30, 40, 200, 25)  # Ustawienie geometrii paska postępu

        self.button = QPushButton('Start', self)
        self.button.move(40, 80)
        self.button.clicked.connect(self.startProgressBar)  # Podłączenie przycisku do metody startProgressBar

        self.timer = QBasicTimer()  # Inicjalizacja timera

        self.progress = 0  # Zmienna przechowująca aktualny postęp

        self.setWindowTitle('Progress Bar Example')
        self.setGeometry(300, 300, 280, 120)
        self.show()

    def timerEvent(self, event):
        if self.progress >= 100:
            self.timer.stop()
            self.button.setText('Finished')
            return

        self.progress += 1
        self.progressbar.setValue(self.progress)  # Ustawienie wartości paska postępu

    def startProgressBar(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)  # Uruchomienie timera
            self.button.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressBarExample()
    sys.exit(app.exec_())
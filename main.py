import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.popup)

    def popup(self,):
        self.popup_window = Popup()
        self.popup_window.exec()


class Popup(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.ui = loadUi('popup.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton.clicked.connect(self.close)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

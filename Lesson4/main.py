import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore
from PyQt6 import uic

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lesson4.ui', self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec())
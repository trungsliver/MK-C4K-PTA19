import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# xử lý
app = QApplication(sys.argv)

class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('signup.ui', self)
        
# Run app
window = Signup()
window.show()
sys.exit(app.exec())
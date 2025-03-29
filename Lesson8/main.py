import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# xử lý
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lesson8.ui', self)
        # Khai báo các sự kiện ấn nút
        # khi thay đổi số lượng vé
        self.spinBox_avenger.valueChanged.connect(self.update_price)
        self.spinBox_up.valueChanged.connect(self.update_price)
        self.spinBox_popcorn.valueChanged.connect(self.update_price)
        self.spinBox_luckybox.valueChanged.connect(self.update_price)
        # nút checkout
        self.pushButton_checkout.clicked.connect(self.checkout)

    # Phương thức cập nhật số tiền khi thay đổi lượng vé
    def update_price(self):
        # Khởi tạo giá cho các sản phẩm
        price = {
            'avenger': 120000,
            'up': 110000,
            'popcorn': 150000,
            'luckyBox': 100000
        }
        # Biến lưu giá trị tổng tiền
        total = 0
        # Tính tiền theo từng sản phẩm
        total += price["avenger"] * int(self.spinBox_avenger.text())
        total += price["up"] * int(self.spinBox_up.text())
        total += price["popcorn"] * int(self.spinBox_popcorn.text())
        total += price["luckyBox"] * int(self.spinBox_luckybox.text())
        # Hiển thị lên lineEdit
        self.lineEdit_total.setText(str(total) + ' VND')

    # Phương thức thanh toán
    def checkout(self):
        # Hiển thị thông báo
        msg_box('Thanh toán thành công', f'Số tiền: {self.lineEdit_total.text()}')


# Hàm hiển thị thông báo
def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Chuyển cửa sổ giao diện
def switch_window(classw):
    global window
    window = classw
    window.show()

# Run app
window = MainWindow()
window.show()
sys.exit(app.exec())
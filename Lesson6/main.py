import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# xử lý
app = QApplication(sys.argv)
users = ['admin:admin']

class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('signup.ui', self)
        # Khai báo thuộc tính nút ấn signup
        self.pushButton_signup.clicked.connect(self.signup_check)
    
    # Khai báo phương thức signup_check
    def signup_check(self):
        # Khai báo thuộc tính sẽ sử dụng
        username = self.lineEdit_username.text().strip()
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_password.text().strip()
        confirm = self.lineEdit_confirm.text().strip()
        checkB = self.checkBox.isChecked()
        # Biến kiểm tra đăng ký
        check = True

        # Thiếu Thông tin
        if username == '' or email == '' or password == '' or confirm == '' or checkB != True:
            check = False
            msg_box('Signup fail', 'Missing information!')
        # Password và confirm không khớp
        elif password != confirm:
            check = False
            msg_box('Signup fail', 'Password and confirm not match!')
        # Đã tồn tại email trong danh sách users
        else:
            for user in users:
                stored_email, stored_password = user.split(':')
                if email == stored_email:
                    check = False
                    msg_box('Signup fail', 'Email already exists!')
                    break
        
        # Kiểm tra xem có đăng ký thành công không
        if check == True:
            # Thêm tài khoản vào danh sách users
            new_acc = f'{email}:{password}'
            users.append(new_acc)
            msg_box('Signup success', 'Signup success!')
            # Chuyển trang
            switch_window(Login())


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.pushButton_login.clicked.connect(self.login_check)

    def login_check(self):
        check = False
        # Khai báo thuộc tính sẽ sử dụng
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_password.text().strip()
        # Kiểm tra thông tin
        for user in users:
            stored_email, stored_password = user.split(':')
            if email == stored_email and password == stored_password:
                check = True
                break
        # Kiểm tra đăng nhập
        if check == True:
            msg_box('Login success', 'Welcome to my app !!!')
            switch_window(Signup())
        else:
            msg_box('Login fail', 'Email or password is incorrect!')


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
window = Signup()
window.show()
sys.exit(app.exec())
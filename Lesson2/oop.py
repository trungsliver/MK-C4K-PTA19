# Mô phỏng lớp Vật nuôi
class Animal:
    # Hàm khởi tạo thuộc tính
    def __init__(self, type, name, age, color):
        # type, name, age, color là thuộc tính
        self.type = type
        self.name = name
        self.age = age
        self.color = color

    # Phương thức hiển thị thông tin
    def display_info(self):
        print(f'''===== THÔNG TIN =====
Loại: {self.type}
Tên: {self.name}
Tuổi: {self.age}
Màu sắc: {self.color}''')
        
    def __str__(self):
        return f'{self.type} - {self.name} - {self.age} - {self.color}'
    
# Bài 1:   
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Phương thức tính chu vi
    def cvi(self):
        return 2 * (self.width + self.height)
    
    # Phương thức tính diện tích
    def dtich(self):
        return self.width * self.height
    
# Bài 2:
class BankAccount:
        # Khởi tạo thuộc tính
    def __init__(self, acc_number, balance):
        # acc_number là số tài khoản ngân hàng
        self.acc_number = acc_number
        # balance là số dư tài khoản
        self.balance = balance

    # Phương thức deposit() - nạp tiền
    def deposit(self, amount):
        # amount - số tiền nạp vào tài khoản
        if amount > 0:
            self.balance += amount
            print('Nạp tiền thành công!')
            print(f'Số dư {self.acc_number}: ${self.balance}')
        else:
            print('Số tiền nạp không hợp lệ!')

    # Phương thức withdraw - rút tiền
    def withdraw(self, amount):
        # amount - số tiền rút ra khỏi tài khoản
        if 0 < amount <= self.balance:
            self.balance -= amount
            print('Rút tiền thành công!')
            print(f'Số dư {self.acc_number}: ${self.balance}')
        else:
            print('Số tiền rút không hợp lệ!')

    def withdraw2(self):
        # amount - số tiền rút ra khỏi tài khoản
        amount = float(input('Nhập số tiền rút: '))

        # Kiểm tra số tiền rút
        while amount <= 0 or amount > self.balance:
            print(f'Số dư: {self.balance}')
            print('Số tiền rút không hợp lệ!')
            amount = float(input('Nhập số tiền rút: '))

        # Rút tiền
        self.balance -= amount
        print('Rút tiền thành công!')
        print(f'Số dư {self.acc_number}: ${self.balance}')

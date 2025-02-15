from oop import Animal, Rectangle, BankAccount

# Khởi tạo object - đối tượng cụ thể
a1 = Animal('Dog', 'Nam', 2, 'brown')
a2 = Animal('Bear', 'Dũng', 4, 'black')
a3 = Animal('Beaver', 'Loopy', 3, 'pink')

# Hiển thị thông tin object
    # Cách 1: sử dụng thuộc tính
print(a1.type, a1.name, a1.age, a1.color)
    # Cách 2: sử dụng phương thức
a2.display_info()
    # Cách 3: sử dụng phương thức có sẵn
print(a3)

# Bài 1: Xây dựng class Rectangle gồm:
# 	- Thuộc tính: width, height
# 	- Phương thức:
# 		+ cvi(): tính chu vi HCN
# 		+ dtich(: tính diện tích HCN
hcn1 = Rectangle(4, 5)
hcn2 = Rectangle(5, 10)
print('\nChu vi HCN1:', hcn1.cvi())
print('Diện tích HCN1:', hcn1.dtich())
print('Chu vi HCN2:', hcn2.cvi())
print('Diện tích HCN2:', hcn2.dtich())

# Bài 2: Xây dựng class BankAccount gồm:
# 	- Thuộc tính: 
# 		+ acc_number (số tài khoản)
# 		+ balance (số dư)
# 	- Phương thức:
# 		+ deposit(): nạp tiền vào tài khoản
# 		+ withdraw(): rút tiền và cập nhật số dư
acc1 = BankAccount('Huy', 1)
print(f'\nSố dư ban đầu: ${acc1.balance}')
    # Nạp tiền
acc1.deposit(50)
    # Rút tiền
acc1.withdraw(30)
acc1.withdraw2()
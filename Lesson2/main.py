from oop import Animal

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

# Bài 2: Xây dựng class BankAccount gồm:
# 	- Thuộc tính: 
# 		+ acc_number (số tài khoản)
# 		+ balance (số dư)
# 	- Phương thức:
# 		+ deposit(): nạp tiền vào tài khoản
# 		+ withdraw(): rút tiền và cập nhật số dư
# Lập trình hướng đối tượng
# OOP - Object oriented programming

# Tổng quát: OOP là cách chúng ta mô phỏng thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (Đối tượng):   Đối tượng cụ thể

# Ví dụ: mô phỏng Human (con người)
    # Thuộc tính (đặc điểm): Tên, tuổi, giới tính,...
    # Phương thức (hành động): ăn, ngủ, nói chuyện, ...

# Khai báo lớp đối tượng
class Human:
    # Khởi tạo giá trị (thuộc tính)
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức (hành động)
    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}, {self.age} tuổi.')

    def sing(self):
        print(f'{self.name} đang hát: "Baby Shark"')

# Khởi tạo 1 đối tượng (object) mới
human1 = Human('Hoang Nam', 14, 'male')
# Truy cập các thuộc tính của đối tượng
print(human1.name)
# Gọi phương thức của đối tượng
human1.introduce()
human1.sing()

# Tính chất kế thừa
class Human:
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}, {self.age} tuổi.')

# lớp kế thừa - lớp con
class Student(Human):
    # Hàm khởi tại giá trị
    def __init__(self, name, age, gender, school):
        # Gọi hàm khởi tạo của lớp cha
        super().__init__(name, age, gender)
        self.school = school

    # Phương thức __str__ để dùng được print()
    def __str__(self):
        return f'Student: {self.name}, {self.age} tuổi, {self.gender}, {self.school}'
    
    # Phương thức giới thiệu bản thân, ghi đè
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}, học tại {self.school}')    

    # Phương thức hiển thị thông tin
    def display_info(self):
        print(f'''
========== THÔNG TIN ==========
Họ tên:         {self.name}
Tuổi:           {self.age}
Giới tính:      {self.gender}
Trường học:     {self.school}
===============================''')
        
    # Phương thức chỉnh sửa thông tin
        # Chỉnh sửa tên
    def edit_name(self):
        new_name = input('Nhập tên mới: ')
        # strip(): xóa khoảng trắng ở đầu và cuối str
        if new_name.strip() == '':
            print('Tên không hợp lệ!')
        else:
            self.name = new_name
            print('Tên đã được cập nhật!')
        self.display_info()

        # Chỉnh sửa tuổi
    def edit_age(self, new_age :int):
        if new_age < 0:
            print('Tuổi không hợp lệ!')
        else:
            self.age = new_age
            print('Tuổi đã được cập nhật!')
        self.display_info()
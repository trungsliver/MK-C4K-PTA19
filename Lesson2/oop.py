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
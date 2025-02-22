from oop import Human, Student
from oop import Animal, Dog

stu1 = Student('Nam', 12, 'male', 'Ngô Quyền')

print(stu1)
# sử dụng phương thức lớp cha
stu1.introduce()
stu1.display_info()
stu1.edit_name()
stu1.edit_age(2)

# Đề bài:
# Tạo class Animal gồm các thuộc tính: tên, loài
# Viết 2 phương thức cho class Animal

# Tạo class Dog kế thừa từ class Animal và có thêm thuộc tính: giống
# Viết 1 phương thức kế thừa từ class Animal (có sửa đổi)
# Viết 1 phương thức mới cho class Dog

# Yêu cầu:
# - Tạo class ở file oop.py
# - Viết chương trình test tại file main.py

a1 = Animal('Loopy', 'Hải ly')
a1.display_info()
a1.eat()

dog1 = Dog('Bơ', 'Chó', 'Shiba')
dog1.display_info()
dog1.eat() 
dog1.edit_name()
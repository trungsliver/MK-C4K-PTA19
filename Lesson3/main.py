from oop import Human, Student

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
from oop import Human, Student

stu1 = Student('Nam', 12, 'male', 'Ngô Quyền')

print(stu1)
# sử dụng phương thức lớp cha
stu1.introduce()
stu1.display_info()
stu1.edit_name()
stu1.edit_age(2)
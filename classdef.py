class student:
    school_name='ABC School'
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("Harry",20)
print('student:',s1.name,s1.age)
print('school name:',student.school_name)
s1.name='Jessa'
s1.age=19
print('student:',s1.name,s1.age)
student.school_name='XYZ School'
print('school name:',student.school_name)

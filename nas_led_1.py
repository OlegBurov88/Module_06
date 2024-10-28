class Human:
    head = True

    def say_hello(self):
        print('Здравствуйте')


class Student(Human):
    head = False

    def about(self):
        print('Я студент')


class Teacher(Student):
    head = Human.head
    pass


human = Human()
print(human.head)

student = Student()
student.about()

print(student.head)
student.say_hello()

teacher = Teacher()
teacher.say_hello()
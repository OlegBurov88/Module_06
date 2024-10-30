class Human:
    head = True
    _legs = True
    __arms = True

    def say_hello(self):
        print('Здравствуйте')

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)

class Student(Human):
    arms = False
    # def about(self):
    #     print('Я студент')


class Teacher(Student):
    pass


human = Human()
human.about()

student = Student()
student.about()
print(dir(human))
print(dir(student))
print(student._Human__arms)
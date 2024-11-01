class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def say_hello(self):
        print('Здравствуйте')

    def info(self):
        print(f'Привет, меня зовут {self.name}')


class StudentGroup:
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)  # аналогично Human.__init__(self, name)
        self.place = place
        super().info()


student = Student('Алексей', 'Урбан', 'Питон 1')
print(Human.mro())
print(Student.mro())

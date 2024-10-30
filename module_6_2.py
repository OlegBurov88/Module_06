class Vehicle:
    __COLOR_VARIANTS = ['BLUE', 'RED', 'GREEN', 'BLACK', 'WHITE']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__MODEL = model
        self.__COLOR = color
        self.__ENGINE_POWER = engine_power

    def get_model(self):
        return f'Модель: {self.__MODEL}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__ENGINE_POWER}'

    def get_color(self):
        return f'Цвет: {self.__COLOR}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__COLOR = new_color.upper()
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

# Свой код для проверки
print()
vehicle2 = Sedan('Oleg', 'Vesta', 'red', 122)
vehicle2.print_info()
vehicle2.set_color('blue')
vehicle2.set_color('yellow')
vehicle2.owner = 'Vladimir'
vehicle2.print_info()

from math import pi, sqrt


class Figure:  # Определяем родительский класс для фигур
    sides_count = 0  # количество сторон в фигуре

    def __init__(self, rgb, *sides):
        self.__sides = list(sides)
        self.__color = list(rgb)
        self.filled = False
        if len(self.__sides) != self.sides_count:  # условия для неправильного ввода кол-ва сторон
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)
        else:
            for i in range(self.sides_count):
                self.__sides[i] = sides[i]

    def get_color(self):  # геттер для цвета
        return self.__color

    def __is_valid_color(self, r, g, b):  # проверка RGB на допустимые значения
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False

    def set_color(self, r, g, b):  # сеттер для изменения цвета
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):  # проверка "сторон"
        for side in new_sides:
            if not (isinstance(side, int) and side > 0):
                return False
        if len(new_sides) != self.sides_count:
            return False
        return True

    def get_sides(self):  # геттер для сторон
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # сеттер для введения новых значений сторон
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):  # Определяем класс для круга
    sides_count = 1  # количество сторон в круге

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.__radius = self.__len__() / 2 * pi

    def get_square(self):  # площадь круга из периметра
        return self.__len__() ** 2 / 4 * pi


class Triangle(Figure):  # Определяем класс для треугольника
    sides_count = 3  # количество сторон в треугольнике

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)

    def get_square(self):  # площадь треугольника по формуле Герона
        a = self._Figure__sides[0]
        b = self._Figure__sides[1]
        c = self._Figure__sides[2]
        p = self.__len__() / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):  # Определяем класс для куба
    sides_count = 12  # количество сторон в кубе

    def __init__(self, rgb, *sides):
        if len(sides) == 1:
            sides *= self.sides_count
        elif len(sides) == self.sides_count and len(set(sides)) > 1:
            print('Это не куб, стороны сброшены на 1')
            sides = [1] * 12
        else:
            sides = [1] * 12
        super().__init__(rgb, *sides)

    def set_sides(self, *new_sides):  # сеттер для введения новых значений сторон
        if len(new_sides) == 1 and new_sides[0] > 0:
            for i in range(self.sides_count):
                self._Figure__sides[i] = new_sides[0]
        elif len(new_sides) == self.sides_count and len(set(new_sides)) > 1:
            print('Это не куб')

    def get_volume(self):  # объём куба
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# # Тест для круга
# print()
# circle_1 = Circle((1, 1, 1), 20)
# circle_2 = Circle((2, 2, 2), 20, 30, 40)
# circle_2.set_color(259, 260, 0)
# print(circle_2.get_color())
# circle_2.set_sides(15)
# print(circle_2.get_sides())
# circle_2.set_sides(10.3)
# print(circle_1.get_sides())
# print(f'Площадь круга = {round(circle_1.get_square(), 2)} кв.ед.')
# print(f'Площадь круга = {round(circle_2.get_square(), 2)} кв.ед.')
#
# # Тест для треугольника
# print()
# triangle_1 = Triangle((1, 1, 1), 10, 10)
# triangle_2 = Triangle((2, 2, 2), 5, 6, 7)
# triangle_1.set_color(10, 10, 10)
# print(triangle_1.get_color())
# triangle_1.set_color(100, 200, 300)
# print(triangle_1.get_color())
# triangle_1.set_sides(10)
# triangle_1.set_sides(20, 3.5, 4)
# triangle_1.set_sides(9, 10, 11)
# print(triangle_2.get_sides())
# print(f'Площадь треугольника = {round(triangle_1.get_square(), 2)} кв.ед.')
# print(f'Площадь треугольника = {round(triangle_2.get_square(), 2)} кв.ед.')
#
# # Тест для куба
# print()
# cube_1 = Cube((1, 1, 1), 9)
# print(f'Объём куба = {round(cube_1.get_volume(), 2)} куб.ед.')
# cube_1.set_sides(2, 2)
# cube_2 = Cube((2, 2, 2), 2, 2)
# cube_2.set_sides(3)
# print(cube_2.get_sides())
# print(f'Объём куба = {round(cube_2.get_volume(), 2)} куб.ед.')

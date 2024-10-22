

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.filled = False
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = [0, 0, 0]

    def __len__(self):
        return sum(self.__sides)

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __is_valid_color(self, r, g, b):
        for x in [r, g, b]:
            if not (isinstance(x, int) and 0 <= x <= 255):
                return False
        return True

    def __is_valid_sides(self, *sides):
        for s in sides:
            if not (isinstance(s, int) and s > 0):
                return False
        if sides.__len__() != self.sides_count:
            return False
        return True

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = self.get_radius()

    def __len__(self):
        return self.get_sides()[0]

    def get_square(self):
        return 3.14 * pow(self.__radius, 2)

    def get_radius(self):
        return self.get_sides()[0] / (2 * 3.14)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        perimetr = 0
        sides = self.get_sides()
        for s in sides:
            perimetr += s
        perimetr = perimetr / 2
        s = perimetr * (perimetr - sides[0]) * (perimetr - sides[1]) * (perimetr - sides[2])
        return pow(s, 0.5)

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1 and isinstance(sides[0], int) and sides[0] > 0:
            valid_sides = [sides[0]] * self.sides_count
        else:
            valid_sides = [1] * self.sides_count
        super().__init__(color, *valid_sides)

    def set_sides(self, *sides):
        if len(sides) == 1 and isinstance(sides[0], int) and sides[0] > 0:
            super().set_sides([sides[0]] * self.sides_count)

    def get_volume(self):
        s = self.get_sides()[0]
        return s * s * s

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((5,6,7), 7,10,2)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print("circle color:", circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print("cube color:",cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(f"cube sides: {cube1.get_sides()}")
circle1.set_sides(15) # Изменится
print(f"circle sides: {circle1.get_sides()}")
triangle1.set_sides(6)
print(f"triangle sides: {triangle1.get_sides()}")
triangle1.set_sides(3, 4, 5)
print(f"triangle sides: {triangle1.get_sides()}")

# Проверка периметра:
print("circle perimetr", len(circle1))
print("cube perimetr", len(cube1))
print("triangle perimetr", len(triangle1))

# Проверка объёма (куба):
print("cube volume", cube1.get_volume())

# Площадь
print(f"circle square {circle1.get_square():.2f}", )
print(f"triangle square {triangle1.get_square():.2f}")

# Радиус круга
print(f"circle radius {circle1.get_radius():.2f}")

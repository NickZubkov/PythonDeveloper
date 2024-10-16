class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
            return
        i = 1
        while i <= new_floor:
            print(i)
            i += 1

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name} ,кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print(f"Внимание! тип {type(other)} не поддерживается методом __eq__")
            return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print(f"Внимание! тип {type(other)} не поддерживается методом __lt__")
            return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print(f"Внимание! тип {type(other)} не поддерживается методом __le__")
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print(f"Внимание! тип {type(other)} не поддерживается методом __gt__")
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print(f"Внимание! тип {type(other)} не поддерживается методом __ge__")
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print(f"Внимание! тип {type(other)} не поддерживается методом __ne__")
            return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print(f"Внимание! тип {type(value)} не поддерживается методом __add__")
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        else:
            print(f"Внимание! тип {type(value)} не поддерживается методом __radd__")
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        else:
            print(f"Внимание! тип {type(value)} не поддерживается методом __iadd__")
            return self


def main():
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)
    h2.go_to(-1)
    h2.go_to(0)

if __name__ == "__main__":
    main()
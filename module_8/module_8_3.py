

class Car:

    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Некорректный тип vin номера")
        elif not (1000000 <= vin <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message

class CarCreator:

    def create_car(self, model, vin, numbers):
        try:
            car = Car(model, vin, numbers)
        except IncorrectVinNumber as exc:
            print(f"Не удалось создать автомобиль: {exc.message}")
        except IncorrectCarNumbers as exc:
            print(f"Не удалось создать автомобиль: {exc.message}")
        else:
            print(f'{car.model} успешно создан')
            return car

car_creator = CarCreator()
first = car_creator.create_car('Model1', 1000000, 'f123dj')
second = car_creator.create_car('Model2', 300, 'т001тр')
third = car_creator.create_car('Model3', 2020202, 'нет номера')
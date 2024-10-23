from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:

    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        info = file.read()
        file.close()
        return info

    def add(self, *products):
        for p in products:
            if isinstance(p, Product):
                if self.get_products().__contains__(p.name):
                    print(f"Продукт {p.name} уже есть в магазине'")
                    continue
                file = open(self.__file_name, "a")
                file.write(f"{p}\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

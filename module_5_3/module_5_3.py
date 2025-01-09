# 2023/10/30 00:00|Домашняя работа по уроку "Специальные методы классов"



class House:                                      # Создайте класс House.
    def __init__(self, name, number_of_floors):   # Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
        self.name = name                          # Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
        self.number_of_floors = number_of_floors
    def __len__(self):                            # дополнить класс House следующими специальными методами: __len__ и __str__
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}" 
    def __eq__(self, other):                       # дополнить класс House следующими специальными методами  __eq__  __add__  __ge__ __lt__ __le__ __ne__ __gt__ __radd__....
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)







    def go_to(self, new_floor):                   # Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")



house = House('ЖК Эльбрус', 30)                    # Создайте объект класса House с произвольным названием и количеством этажей.
house2 = House('ЖК Тор', 44)  

# __str__
print(house)
print(house2)
# __len__
print(len(house))
print(len(house2))
# __eq__
print(house == house2)
# __add__
h1 = house + 10
print(house)
print(house == house2)
# __iadd__
house += 10
print(house)
# __radd__
house2 = 10 + house2
print(house2)
# __gt__
print(house > house2)
# __ge__
print(house >= house2)
# __lt__
print(house < house2)
# __le__
print(house <= house2)
# __ne__
print(house != house2)
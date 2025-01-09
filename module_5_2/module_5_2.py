# 2023/10/30 00:00|Домашняя работа по уроку "Специальные методы классов"



class House:                                      # Создайте класс House.
    def __init__(self, name, number_of_floors):   # Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
        self.name = name                          # Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
        self.number_of_floors = number_of_floors
    def __len__(self):                            # дополнить класс House следующими специальными методами: __len__ и __str__
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"



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
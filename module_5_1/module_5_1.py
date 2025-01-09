# 2023/10/29 00:00|Домашняя работа по уроку "Атрибуты и методы объекта"

class House:                                      # Создайте класс House.
    def __init__(self, name, number_of_floors):   # Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
        self.name = name                          # Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):                   # Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")


house = House('ЖК Эльбрус', 30)                    # Создайте объект класса House с произвольным названием и количеством этажей.
house2 = House('ЖК Тор', 44)  

house.go_to(10)                                    # Вызовите метод go_to у этого объекта с произвольным числом.
house.go_to(350)

house2.go_to(8)                                    # Вызовите метод go_to у этого объекта с произвольным числом.
house2.go_to(66)
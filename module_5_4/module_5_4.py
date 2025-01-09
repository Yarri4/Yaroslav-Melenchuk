# 2023/11/02 00:00|Домашняя работа по уроку "Различие атрибутов класса и экземпляра"



class House:                      # Создайте класс House.
    houses_history = []           # В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

    def __new__(cls, *args):
        obj = super().__new__(cls)
        house_name = args[0]
        cls.houses_history.append(house_name)
        return obj
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Дом '{self.name}' снесён, но он останется в истории.")
        
house1 = House('ЖК Эльбрус')
print(House.houses_history)
house2 = House('ЖК Акация')
print(House.houses_history)
house3 = House('ЖК Матрёшки')
print(House.houses_history)

del house2
del house3
del house1
print(House.houses_history)
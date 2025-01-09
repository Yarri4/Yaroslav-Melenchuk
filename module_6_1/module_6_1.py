# 2023/11/07 00:00|Домашнее задание по теме "Зачем нужно наследование"


class Animal:                   # 1 класс родителя
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:                    # 2 класс родителя
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
            print(f"{self.name} сыто")
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
            print(f"{self.name} мертво")

class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
            print(f"{self.name} сыто")
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
            print(f"{self.name} мертво")

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
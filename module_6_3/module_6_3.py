# 2023/11/09 00:00|Домашнее задание по теме "Множественное наследование"

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            return "Sorry, I'm peaceful :)"
        else:
            return f"Be careful, I'm attacking you 0_0"


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        return "Here are(is) eggs for you"


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)  # берем модуль
        if self._cords[2] - dz * (self.speed / 2) < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] -= dz * (self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


# Пример использования
if __name__ == "__main__":
    duckbill = Duckbill(10)
    print(duckbill.get_cords())

    duckbill.move(1, 1, -1)
    print(duckbill.get_cords())

    duckbill.move(1, 1, -10)  # Слишком глубокое погружение
    print(duckbill.attack())  
    duckbill.lay_eggs()


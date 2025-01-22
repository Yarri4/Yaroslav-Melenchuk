# 2023/10/18 00:00|Домашняя работа по уроку "Модули и пакеты"


from fake_divide import fake_divide as fake_divide
from true_divide import true_divide as true_divide


result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
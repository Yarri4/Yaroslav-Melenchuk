# 2023/10/18 00:00|Домашняя работа по уроку "Модули и пакеты"


from fake_math import divide as fk_div
from true_math import divide as tr_div

print('result1 = ', fk_div(12, 4))
print('result2 = ', fk_div(12, 0))
print('result3 = ', tr_div(13, 5))
print('result4 = ', tr_div(13, 0))
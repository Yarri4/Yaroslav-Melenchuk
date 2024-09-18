# 2023/10/01 00:00|Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]


my_list_zero = 0

while my_list_zero < len(my_list):
    new_list = my_list[my_list_zero]
    my_list_zero = my_list_zero + 1
    if new_list < 0:
        print('Отрицательное число:', new_list)
        break
    elif new_list == 0:
        continue
    elif new_list == len(my_list):
        print(new_list)
        print('Конец списка')
    else:
        print(new_list)
# 2023/09/29 00:00|Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second and second == third and third == first:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
# 2023/11/29 00:00|Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results.update({func.__name__: func(int_list)})
    return results

int_list = [1, 4, 45.321, -555, 999.999, 112, 3]

def min(int_list):  # - принимает список, возвращает минимальное значение из него.
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] < int_list[i + 1]:
            result = int_list[i]
    return result

def max(int_list):  # - принимает список, возвращает максимальное значение из него.
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] > int_list[i + 1]:
            result = int_list[i]
    return result

def len_(int_list):  # - принимает список, возвращает кол-во элементов в нём.
    result = len(int_list)
    return result

def sum(int_list):  # - принимает список, возвращает сумму его элементов.
    result = 0
    for i in int_list:
        result += i
    return result

def sorted_(int_list):  # - принимает список, возвращает новый отсортированный список на основе переданного.
    result = sorted(int_list)
    return result

def midle(int_list):  # - принимает список, возвращает среднее значение его элементов.
    result = 0
    for i in int_list:
        result += i
    result = result / len_(int_list)
    return result


print(apply_all_func(int_list, min, max, sum, midle))
print(apply_all_func(int_list, len_, sorted_))
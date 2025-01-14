# 2023/11/24 00:00|Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    try:
        result = a + b
        return result
    except TypeError:   #  возвращать строковое представление этих двух данных вместе
        if type(a) == int or isinstance(a, float) and type(b) == str:
                result = str(a) + b
        elif type(a) == str and isinstance(b, int) or isinstance(b, float):
                result = a + str(b)
    return result

print(add_everything_up(10, 2.5))
print(add_everything_up(123, 'Дом'))
print(add_everything_up('Лом', 2.5))


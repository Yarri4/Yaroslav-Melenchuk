# 2023/12/05 00:00|Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, result):
                if (result % i) == 0:
                    print(f"Составное число {result}")
                    break
            else:
                print(f"Простое число {result}")
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

sum_three(1, 1, 1)
sum_three(3, 3, 3)
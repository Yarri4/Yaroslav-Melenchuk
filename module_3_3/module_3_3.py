# 2023/10/09 00:00|Самостоятельная работа по уроку "Распаковка позиционных параметров"


# 1.Функция с параметрами по умолчанию:
def print_params(a = 2, b = 'строка', c = True):
    print(a, b, c)

# Вызов функции print_params.
print_params(6, 'Tomas')
print_params( 12,None, False)
print_params(24)
print_params()

# Проверка.
print_params(b=25)
print('Функция print_params(b=25) работает')
print_params(c = [1,2,3])
print('Функция print_params(c = [1,2,3]) работает')
# 2.Распаковка параметров:
# список
values_list = [125, None, 'Текст']
# словарь 
values_dict = {'a':3216.2431, 'b':"Куст", 'c':False}

# Передача параметров
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка']
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)
print('Функция print_params(*values_list_2, 42) работает')
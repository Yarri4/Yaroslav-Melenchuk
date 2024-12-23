# 2023/10/24 00:00|Домашняя работа по уроку "Пространство имен."


def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        
    inner_function() 

test_function() # Я в области видимости функции test_function

inner_function() # name 'inner_function' is not defined. Did you mean: 'test_function'?
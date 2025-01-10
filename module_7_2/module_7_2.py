# 2023/11/16 00:00|Домашнее задание по теме "Позиционирование в файле".

from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')

    string_positions = {}   # создан словарь
    str_num = 0
    str_start_byte = file.seek(0)
    
    for string_ in strings:
        file.write(string_+'\n')
        str_num += 1
        key = (str_num, str_start_byte) # ключи словаря
        string_positions[key]= string_  # значения в словаре
        str_start_byte = file.tell()
    file.close()
    return string_positions

file_name = 'text_for_7_2.txt'   # создание файла 
strings = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write(file_name, strings)
pprint(result)  # выводим результат для проверки
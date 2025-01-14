# 2023/11/19 00:00|Домашнее задание по теме "Файлы в операционной системе".


import os, time
from os.path import join, getmtime, getsize, dirname
directory = "."     # тестировать будем в папке проекта
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        # parent_dir = os.path.dirname(os.path.abspath(file)) # полный путь
        parent_dir = os.path.dirname(directory)  # относительный путь
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
# 2023/11/26 00:00|Домашнее задание по теме "Создание исключений"

import time
from multiprocessing import Pool

# Список названий файлов из архива к задаче
file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt','file 4.txt']

# Функция для чтения данных из файла
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline() # Читаем файл
            if not line:  # Выход из цикла
                break
            all_data.append(line.strip())  # Добавляем строку

if __name__ == '__main__':
    start_time_parallel = time.time()

    with Pool() as pool:
        results = pool.map(read_info, file_names)

    end_time_parallel = time.time()
    print(f"Время выполнения многопроцессного подхода: {end_time_parallel - start_time_parallel:.2f} секунд")
# 2023/12/05 00:00|Домашнее задание по теме "Декораторы"

import threading
import time

def write_words(word_count, file_name):
    start_time = time.time()
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}'
            file.write(word + '\n')
            time.sleep(0.1)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Завершилась запись в файл {file_name}. Время работы потока: {execution_time} секунд')

# Пример использования функции
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Создание потоков
thread1 = threading.Thread(target=write_words, args=(10, 'example1.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example2.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example3.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example4.txt'))

# Запуск потоков
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()
thread3.join()
thread4.join()
# 2024/01/15 00:00|Домашнее задание по теме "Асинхронность на практике"

import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    
    for i in range(1, 6):  # 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар.')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    # Создание задач для каждого силача
    tasks = [
        asyncio.create_task(start_strongman('Pasha', 3)),
        asyncio.create_task(start_strongman('Denis', 4)),
        asyncio.create_task(start_strongman('Apollon', 5))
    ]
    
    # Ожидание задач
    await asyncio.gather(*tasks)

# Запуск функции
asyncio.run(start_tournament())


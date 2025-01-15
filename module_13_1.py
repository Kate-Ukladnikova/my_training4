# Задание по теме "Асинхронность на практике"
# Цель: приобрести навык использования асинхронного запуска функций на практике.
# "Асинхронные силачи": необходимо сделать имитацию соревнований по поднятию шаров Атласа.

import asyncio

async def start_strongman(name, power):
    # name - name - имя силача, power - его подъёмная мощность.
    print(f"Силач {name} начал соревнования.")
    for i in range(1,6):
        await asyncio.sleep(delay=1/power)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    task1=asyncio.create_task(start_strongman('Pasha', 3))
    task2= asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
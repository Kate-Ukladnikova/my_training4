# "Многопроцессное программирование"
# Цель: понять разницу между линейным
# и многопроцессным подходом, выполнив операции обоими способами.
# Задача "Многопроцессное считывание"

import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line != "":
            all_data.append(line)
            line = file.readline()

filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вызов

tn = time.time()
for name in filenames:
    read_info(name)
te = time.time()
t_rez = te - tn
print(f'{t_rez} (линейный)')

# Многопроцессный

# if __name__ == '__main__':
#     tn = time.time()
#     with Pool() as p:
#         rez = p.map(read_info, filenames)
#     te = time.time()
#     t_rez = te - tn
#
#     print(f'{t_rez} (многопроцессный)')







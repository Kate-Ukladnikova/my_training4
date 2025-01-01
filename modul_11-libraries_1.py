# Библиотеки pandas, numpy

import numpy as np
import pandas as pd

file = open('primer.txt', 'r')
stroka = '1'
arr = []

# считываем из файла primer.txt все строки и, если их возможно перевести
# в разряд чисел с плавающей запятой, то переводим, если же нет -
# ловим исключение и записываем в эту ячейку массива NaN вместо строки-нечисла
# c помощью библиотеки numpy.

while stroka != '':
    stroka = file.readline()
    try:
        if stroka == '':
            break
        arr.append(float(stroka))
    except ValueError as exc:
        arr.append(np.nan)
file.close()

# pd.Series
# создание объекта: одномерный маркированный массив, содержащий данные любого типа

s = pd.Series(arr)
print(s)

# pandas.DataFrame
# создание двумерного массива данных из словаря

file2 = open('primer2.txt', 'r')
stroka0 = '1'
dict = dict()

while stroka0 != '':
    stroka0 = file2.readline()
    if stroka0 != '':
        stroka = stroka0.split(':')
        dict[stroka[0]] = [int(i) for i in stroka[1].split(',')]
file2.close()
df = pd.DataFrame(data=dict)
print(df)
df = pd.DataFrame(data=dict, dtype=np.int8)
print(df.dtypes)
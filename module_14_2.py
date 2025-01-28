# Тема: "Выбор элементов и функции в SQL запросах".

import sqlite3
from distutils.util import execute

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Заполняю таблицу Users 10 записями:
# for user in range(1,11):
#    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
#    (f"User{user}",f"example{user}@gmail.com", user*10, 1000))

# Обновляю balance у каждой 2ой записи начиная с 1ой на 500:
# cursor.execute("UPDATE Users SET balance = ? WHERE id%2 != 0", (500, ))

# Удаляю каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1,11):
#     if i==1 or (i-1)%3 == 0:
#         cursor.execute("DELETE from Users WHERE username = ?", (f"User{i}", ))

# Выборка из всех записей, где возраст не равен 60:
# cursor.execute("SELECT * FROM Users")
# users = cursor.fetchall()
# for user in users:
#    user = list(user)
#    if user[3]==60:
#       continue
#    else:
#       print('Имя:', user[1], '|', 'Почта:', user[2], '|', 'Возраст:', user[3], '|',
#             'Баланс:', user[4] )

# Удаление пользователя с id=6
cursor.execute("DELETE from Users WHERE id = ?", (6, ))

# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances/total_users)
connection.commit()
connection.close()
# "Создание БД, добавление, выбор и удаление элементов"
# Oсвоить основные команды языка SQL и использовать
# их в коде, используя SQLite3.
# Задача "Первые пользователи".

import sqlite3

# Для работы с базой данных через DB Browser подключaюсь
# к ней, чтобы выполнять различные операции. Для этого создам соединение
# (connection).

connection = sqlite3.connect("not_telegram.db")

# Cоздам так называемый «cursor». Это можно представить
# как виртуальную "мышку", которая помогает работать с базой данных.

cursor = connection.cursor()

# Для обращения к базе данных использую команду 'execute',
# которая позволяет транслировать SQL-запросы напрямую в базу данных.
# Сейчас буду писать SQL-запросы —
# это отдельный язык, предназначенный для взаимодействия с базами данных.

# Создаю таблицу Users:

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
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
   user = list(user)
   if user[3]==60:
      continue
   else:
      print('Имя:', user[1], '|', 'Почта:', user[2], '|', 'Возраст:', user[3], '|',
            'Баланс:', user[4] )

# После выполнения процесса сохраняю изменения в базе данных.
# Для этого использую команда 'connection.commit',
# которая фиксирует текущее состояние и сохраняет все изменения
# ('commit' позволит сохранить состояние).

connection.commit()

# После сохранения закрываю соединение с базой данных,
# чтобы освободить ресурсы.

connection.close()
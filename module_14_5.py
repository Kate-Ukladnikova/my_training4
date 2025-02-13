# Тема "Написание примитивной ORM".
# Цель: написать простейшие CRUD функции для взаимодействия с базой данных.
# Задача "Регистрация покупателей".

import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api =""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
button3 = KeyboardButton(text = 'Купить')
button4 = KeyboardButton(text = 'Регистрация', callback_data = 'registration_had_finished')
start_menu.add(button, button2, button3, button4)

kb = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text = 'Product1', callback_data = 'product_buying')
button2 = InlineKeyboardButton(text = 'Product2', callback_data = 'product_buying')
button3 = InlineKeyboardButton(text = 'Product3', callback_data = 'product_buying')
button4 = InlineKeyboardButton(text = 'Product4', callback_data = 'product_buying')
kb.add(button, button2, button3, button4)

connection = sqlite3.connect("not_telegram_products2.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products2(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
)
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
)
''')
initiate_db()
# Заполняю таблицу Products2 4-мя записями:
# for product in range(1,5):
#    cursor.execute("INSERT INTO Products2(title, description, price) VALUES(?, ?, ?)",
#                   (f"Продукт{product}",f"Описание{product}", product*100))

# Создаю функцию add_user(username, email, age), которая принимает: имя пользователя, почту и возраст.
# Данная функция должна добавлять в таблицу Users моей
# БД запись с переданными данными. Баланс у новых пользователей всегда равен 1000.

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = start_menu)

def add_user(username, email, age):
    print(username, email, age)
    cursor.execute("SELECT max(id) FROM Users")
    cur = cursor.fetchone()[0]
    print(cur)
    if cur == None:
        currId=1
    else:
        currId = cur+1

    cursor.execute("INSERT INTO Users (id, username, email, age, balance) values(?,?,?,?,?) ", (currId, username, email, age, 1000))

    connection.commit()
    connection.close()

def is_included(username):
    cursor.execute("SELECT * FROM Users")
    total_users = cursor.fetchall()
    ans = False
    for i in range(0, len(total_users)):
        if total_users[i][1] == username:
            ans = True
            break
        else:
            ans = False
    return ans

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text = ['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя:')
        await state.set_state(RegistrationState.username)
        await RegistrationState.username.set()
        RegistrationState.username = message.text
    else:
        RegistrationState.username = message.text
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@dp.message_handler(state = RegistrationState.email)
async def set_email(message, state):
    RegistrationState.email = message.text
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state = RegistrationState.age)
async def set_age(message, state):
    RegistrationState.age = message.text
    add_user(RegistrationState.username, RegistrationState.email, RegistrationState.age)
    await state.finish()

@dp.callback_query_handler(text=['registration_had_finished'])
async def send_finish_message(call):
    await call.answer('Регистрация прошла успешно!')

def get_all_products():
    cursor.execute("SELECT * FROM Products2")
    total_products = cursor.fetchall()
    return total_products

@dp.message_handler(text = ['Купить'])
async def get_buying_list(message):
    p = get_all_products()
    for number in range(0,len(p)):
        await message.answer(f'Название: Product{p[number][1]} | Описание: {p[number][2]} | Цена: {p[number][3]}')
        with open(f'{number}.png', "rb") as img:
            if number==0:
                await message.answer_photo(img, 'Картошка')
            elif number==1:
                await message.answer_photo(img, 'Капуста')
            elif number==2:
                await message.answer_photo(img, 'Морковка')
            elif number==3:
                await message.answer_photo(img, 'Кабачки')
    await message.answer('Выберите продукт для покупки:', reply_markup = kb)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



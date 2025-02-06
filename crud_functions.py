# "План написания админ панели".
# Написать простейшие CRUD функции для взаимодействия с базой данных.
# Задача "Продуктовая база".

import sqlite3
from distutils.util import execute
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api =""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
button3 = KeyboardButton(text = 'Купить')
start_menu.add(button, button2, button3)

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
initiate_db()
# Заполняю таблицу Users 4-мя записями:
# for product in range(1,5):
#    cursor.execute("INSERT INTO Products2(title, description, price) VALUES(?, ?, ?)",
#                   (f"Продукт{product}",f"Описание{product}", product*100))

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

connection.commit()
connection.close()


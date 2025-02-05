# "Доработка бота": подготовить Telegram-бота для взаимодействия с базой данных.
# "Витамины для всех!"

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

@dp.message_handler(text = ['Купить'])
async def get_buying_list(message):
    for number in range(0,4):
        await message.answer(f'Название: Product{(number+1)} | Описание: овощ {(number+1)} | Цена: {(number+1) * 100}')
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

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я - бот, помогающий твоему питанию.', reply_markup = start_menu)

@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb=ReplyKeyboardMarkup(resize_keyboard=True)
button=KeyboardButton(text='Рассчитать')
button1=KeyboardButton(text='информация')
kb.row(button, button1)

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)



class UserState(StatesGroup):
    age=State()
    growth=State()
    weight=State()

@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await UserState.weight.set()
    await state.update_data(weight=message.text)
    data=await state.get_data()
    res=10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age'])+5
    await message.answer(str(res))
    await state.finish()


@dp.message_handler()
async def unstart_messge(message):
    await message.answer('введите команду /start для начала работы бота')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "8156035056:AAGQmHrqza1T7UcW2vaR--XQJjTl_fpwt2E"
bot = Bot(token = api)
dp = Dispatcher(bot,storage= MemoryStorage())


@dp.message_handler(commands=['start'])
async def urban_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    
    
@dp.message_handler(text = ['Urban','ff'])
async def urban_message(message):
    print("Urban message")
    
    
@dp.message_handler()
async def urban_message(message):
    print("Top message")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
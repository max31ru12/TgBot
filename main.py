import logging
# import asyncio
from aiogram import Bot, Dispatcher, types, executor

# Base bot's configurations
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token='5825399743:AAH34T1CqNIWaUyYR3j7hjIDp3TqD8CnzRk')
# Диспетчер
dp = Dispatcher(bot)


# message.text - это текст сообщения
# dp.message_handler allows me to take all message
@dp.message_handler()
# message - то, что отправляет нам клиент
async def echo(message: types.Message):
    # message.answer - написать сообщение (не reply)
    await message.answer(text=message.text)
# types.Message - это привязка к объекту класса Message


if __name__ == '__main__':
    # Запускаем бота в режиме поллинга
    executor.start_polling(dp, skip_updates=True)

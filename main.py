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
# # message.text - это текст сообщения
# # dp.message_handler allows me to take all message
# @dp.message_handler()
# # message - то, что отправляет нам клиент
# async def echo(message: types.Message):
#     # message.answer - написать сообщение (не reply)
#     await message.answer(text=message.text)
# # types.Message - это привязка к объекту класса Message

HELP_COMMAND = '''
/help - список команд
/start - начать работу с ботом
'''


# Функция, которая выполняется, когда включается бот
async def on_start_up(_):
    print('Бот был успешно запущен')


# Обрабатываем команду \help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(HELP_COMMAND)
    # # Delete last message
    # await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Поддерживает какую-то неадекватную HTML-разметку
    await message.answer('<a>Привет!</a>', parse_mode='HTML')


@dp.message_handler(commands=['give'])
async def sticker_message(message: types.Message):
    print(message.from_user.id)
    await bot.send_sticker(message.from_user.id, sticker='')


if __name__ == '__main__':
    # Запускаем бота в режиме поллинга
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)

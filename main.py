import logging
# import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


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

# Создаем клавиатуру
# resize_keyboard - подстраивает клавиатуру под ТГ более красиво (default - False)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
# Добавляем в клавиатуру кнопку
kb.add(KeyboardButton('/help'))
botton_two = KeyboardButton('/photo')
botton_three = KeyboardButton('/give')
# Добавляет новую клавищу (на новую линию)
kb.add(botton_two)
# Добавляет новую кнопку (в новый стобец последней строки)
kb.insert(botton_three)


# Функция, которая выполняется, когда включается бот
async def on_start_up(_):
    print('Бот был успешно запущен')


# START-command
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Поддерживает какую-то неадекватную HTML-разметку (типа курсив)
    await message.answer('<em>Привет!</em>',
                         parse_mode='HTML',
                         reply_markup=kb)
# reply_markup - сюда передается клавиатура, которую нужно создать заранее


@dp.message_handler(commands=['echo'])
async def echo(message: types.Message):
    # The line located below allow to answer message (not reply) in current chat
    # where object message appeared
    await message.answer(text=message.text)
    # This line allows to send message in different chat calling them by their's id (chat_id = ...)
    await bot.send_message(text=message.text,
                           chat_id=message.chat.id)
    # the line below send text message to user in ЛС, who sended command in group chat
    await bot.send_message(text="I'm writing this code at 1:55", chat_id=message.from_user.id)


@dp.message_handler(commands=['photo'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://31.img.avito.st/image/1/otJJkLaxDjt_J4w2AbrZxb0zDj_1MQQ5")


# Обрабатываем команду \help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(HELP_COMMAND,
                        reply_markup=ReplyKeyboardRemove())
    # ReplyKeyboardRemove - удаляет клавиатуру по этой команде
    # # Delete last message
    # await message.delete()


@dp.message_handler(commands=['give'])
async def sticker_message(message: types.Message):
    print(message.from_user.id)
    await bot.send_sticker(message.from_user.id, sticker='')


if __name__ == '__main__':
    # Запускаем бота в режиме поллинга
    # skip_updates = False (так по умолчанию)- юзер пиишет боту, бот не онлайн, когла
    # бот заходит, то отвечает на все сообщения
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)

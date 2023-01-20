from aiogram import types, Dispatcher, Bot
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


# Объект бота
bot = Bot(token='5825399743:AAH34T1CqNIWaUyYR3j7hjIDp3TqD8CnzRk')
# Диспетчер
dp = Dispatcher(bot)

HELP_COMMAND = '''
/help - список команд
/start - начать работу с ботом
/buy - каталог товаров
/
'''

goods_list = {
    'Кроссовки': {'photo_link': 'https://cdn1.ozone.ru/s3/multimedia-c/6233935680.jpg',
                  'description': 'Boots description'},
    'Свитеры': {'photo_link': 'https://ae04.alicdn.com/kf/Hc6477cb31ed14f97a031e60f3c889bcaS/JuneLove.jpg_640x640.jpg',
                'description': 'Sweater desription'},
    'Штаны': {'photo_link': 'https://coxshop.ru/upload/iblock/d57/d57f20a5883a904ad599263679ee02c4.jpg',
              'description': 'pants description'},
}
# Временное решение для отслеживания созданных кнопок
botton_count = 0
catalog_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

for key in goods_list.keys():
    if (botton_count == 0) or (botton_count % 4 == 0):
        catalog_keyboard.add(f'/{key}')
    else:
        catalog_keyboard.insert(f'/{key}')
    botton_count += 1


@dp.message_handler(commands='Кроссовки')
async def boots(message: types.Message):
    await message.answer(text='Some description', )








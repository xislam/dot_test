from aiogram import Dispatcher, Bot, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from django.core.management.base import BaseCommand


from api_for_bot.models import APIData

bot = Bot(token='5075416820:AAGW151xNrHTnHiEYWo5jA0xg6O7R-Brog8')
dp = Dispatcher(bot)

button = KeyboardButton('День рождения👋')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! это тестовая задача что бы увидеть слова напишите любое слово", reply_markup=greet_kb)


@dp.message_handler()
async def post(message: types.Message, ):
    text = message.text
    if text:
        data = list(APIData.objects.all())
        for item in data:
            server_number = item.server_number
            modem_number = item.modem_number
            city = item.city
            operator = item.operator
            data_time = item.data_time
            if item.sent == False:
                await bot.send_message(message.chat.id, text=f'\n'
                                                             f'№ Сервера:{server_number}\n'
                                                             f'№ Модема:{modem_number}\n'
                                                             f'Город:{city}\n'
                                                             f'Оператор:{operator}\n'
                                                             f'Время:{data_time}\n'
                                       )
                item.sent = True
                item.save()


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        executor.start_polling(dp)

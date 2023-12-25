from aiogram import executor
from aiogram import types, filters
from config import dp
from aiogram import Bot, Dispatcher
from config import (biz_haqimizda,
                    nega_aynan_biz, 
                    boglanish_buxoro, 
                    boglanish_navoiy , 
                    ijtimoiy_tarmoqlar,
                    muolaja_haqida)
from Data_base import user
from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests
from environs import Env

env = Env()
env.read_env()


'''
Bahrom Bek 2023 Oktabr
Telegram: @bahrombek19
'''



API_Key = env.str("BOT_TOKEN")
storage = MemoryStorage()
bot = Bot(token=API_Key)
dp = Dispatcher(bot, storage=storage)


# 3 States
class NewTemplate(StatesGroup):
    city = State()
    full_name = State()
    phone_number = State()


# Buttons list
buttonslist = ['🏥 Biz haqimizda', "📞 Biz bilan bog'lanish", '❔ Nega aynan biz', '📍 Bizning manzil', "📅 Doktor ko'rigiga yozilish", "📄 Muolaja haqida malumot", "🍎 Parhez haqida malumotlar",
          '💳 Narxlar']
kb = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
button_list = [types.reply_keyboard.KeyboardButton(text=x) for x in buttonslist]

kb.add(*button_list)

# Filiallar uchun manzil buttonlari
kb_manzil = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
lokatsiyalist = [types.reply_keyboard.KeyboardButton('📍 Buxoro'),
                 types.reply_keyboard.KeyboardButton('📍 Navoiy')]

kb_manzil.add(*lokatsiyalist)

# shifokor ko'rigiga yozilish uchun manzil bilan adashib ketmaydi
kb_shifokor_manzil = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
lokatsiyalist_korik = [types.reply_keyboard.KeyboardButton('Buxoro'),
                 types.reply_keyboard.KeyboardButton('Navoiy')]

kb_shifokor_manzil.add(*lokatsiyalist_korik)


# Inline keyboard
inline_kb = types.InlineKeyboardMarkup(row_width=1)
inline_kb_1 = types.InlineKeyboardButton('Xabar yuborish', url='https://t.me/ibnsino2015')
inline_kb_2 = types.InlineKeyboardButton('Telegram guruhimiz', url='https://t.me/ibnsinobuxoro')
inline_kb_3 = types.InlineKeyboardButton('Instagram', url='https://instagram.com/ibnsino_salomatlik_markazi?igshid=MzRlODBiNWFlZA==')
inline_kb.add(inline_kb_1, inline_kb_2, inline_kb_3)





ID = '1107759940'
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(text='Ibn Sino salomatlik markazi botiga xush kelibsiz', reply_markup=kb)

    if str(message.from_user.id) in user.user_number():
        print('This is old user')
    else:
        tg_id = message.from_user.id
        username = message.from_user.full_name
        # dd/mm/YY H:M:S
        now = datetime.now()
        created_at = now.strftime("%d/%m/%Y %H:%M:%S")
        # Getting exact time when user started
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f'User[{tg_id},{username}]: Started bot at [{current_time}] \n'


        try:
            user.add(tg_id, username,created_at)
            print('New member added to the database')
        except:
            print('Member already exists in the database')




    # write time to file
    with open('log.txt', 'a') as f:
        f.write(message)
        f.close()



    


@dp.message_handler(filters.Text(contains='🏥 Biz haqimizda'))
async def about_us(message: types.Message):
    path = f'ibnsino.jpg'
    path = open(file=path, mode='rb')
    template = types.InputFile(path)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=template,
        reply_markup=kb,
        caption=biz_haqimizda)


@dp.message_handler(commands=['help'])
async def about_us(message: types.Message):
    
    await message.answer(message.chat.id)


@dp.message_handler(filters.Text(contains="📞 Biz bilan bog'lanish"))
async def contact(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=ijtimoiy_tarmoqlar,
        reply_markup=inline_kb
    )



@dp.message_handler(filters.Text(contains="❔ Nega aynan biz"))
async def contact(message: types.Message):
    path = 'nega_aynan_biz.jpg'
    path = open(file=path, mode='rb')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=path,
        reply_markup=kb,
        caption=nega_aynan_biz)
    

@dp.message_handler(filters.Text(contains='📍 Bizning manzil'))
async def about_us(message: types.Message):
    
    await message.answer(text='Iltimos shaharni tanlang', reply_markup=kb_manzil)
    

@dp.message_handler(filters.Text(contains="Muolaja haqida malumot"))
async def parhez(message: types.Message):
    await message.answer(text=muolaja_haqida, reply_markup=kb)


@dp.message_handler(filters.Text(contains="🍎 Parhez haqida malumot"))
async def parhez(message: types.Message):
    path = 'parhez.pdf'
    path = open(file=path, mode='rb')
    await bot.send_document(chat_id=message.from_user.id, document=path)


@dp.message_handler(filters.Text(contains="💳 Narxlar"))
async def parhez(message: types.Message):
    path = 'narxlar.png'
    path = open(file=path, mode='rb')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=path,
        reply_markup=kb
    )


# Doktor ko'rigiga yozilish uchun 3 ta malumot ketma-ketligi
@dp.message_handler(filters.Text(contains="📅 Doktor ko'rigiga yozilish"))
async def contact(message: types.Message):
    await NewTemplate.city.set()
    await message.reply(
        text='🌆 Shaxarni tanlang',
        reply_markup=kb_shifokor_manzil)
    

# Toliq ismingizni kiriting
@dp.message_handler(state=NewTemplate.city)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await message.answer("To'liq ismingizni kiriting", reply_markup=types.ReplyKeyboardRemove())
    await NewTemplate.next()


# Telefon raqamingizni kiriting
@dp.message_handler(state=NewTemplate.full_name)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text
    await message.answer("Telefon raqamingizni kiriting")
    await NewTemplate.next()


# Malumotlarni adminlarga jonatish
@dp.message_handler(state=NewTemplate.phone_number)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    # data base

    await message.answer("Siz shifokor ko'rigiga ro'yxatga olindingiz! \nTez orada siz bilan bog'lanamiz", reply_markup=kb)

    developer = env.str("DEVELOPER")
    admin_buxoro = env.str("ADMIN_BUXORO")
    admin_navoiy = env.str("ADMIN_NAVOIY")
    api_token = API_Key  # Replace with your Telegram bot API token

    city = data['city']
    full_name = data['full_name']
    phone_number = data['phone_number']
    now = datetime.now()
    created_at = now.strftime("%d/%m/%Y %H:%M:%S")

    text = f"Shahar: {city}\nIsmi: {full_name}\nTelefon raqami: {phone_number}\nRo'yhatdan o'tgan sana: {created_at}"

    
    api_url = f"https://api.telegram.org/bot{api_token}/sendMessage"

    if city == '📍 Buxoro':
        admin = admin_buxoro
    else:
        admin = admin_navoiy

    # Send message to developer
    payload = {
        'chat_id': developer,
        'text': text
    }
    
    response = requests.post(api_url, json=payload)

    # Send message to admin
    payload1 = {
        'chat_id': admin,
        'text': text
    }
    
    response1 = requests.post(api_url, json=payload1)

    await state.finish()



# Buxoro locatsiyasi
@dp.message_handler(filters.Text(contains="📍 Buxoro"))
async def contact(message: types.Message):
    path = 'buxoro.jpg'
    path = open(file=path, mode='rb')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=path,
        reply_markup=kb,
        caption=boglanish_buxoro
    )
    longitude =  64.4024167
    latitude = 39.7471944
    await bot.send_location(chat_id=message.from_user.id, 
        latitude=latitude, 
        longitude=longitude)
    

# Navoiy locatsiyasi
@dp.message_handler(filters.Text(contains="📍 Navoiy"))
async def contact(message: types.Message):
    path = 'navoiy.jpg'
    path = open(file=path, mode='rb')
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=path,
        reply_markup=kb,
        caption=boglanish_navoiy
    )

    longitude = 65.35073398011772
    latitude = 40.13138896114748

    await bot.send_location(chat_id=message.from_user.id, 
        latitude=latitude, 
        longitude=longitude)
    


async def on_startup(_):
    print('Bot is online')


if __name__ == '__main__':
    from aiogram.utils import exceptions

    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except exceptions.TerminatedByOtherGetUpdates:
        pass

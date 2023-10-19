from aiogram import executor
from aiogram import types, filters
from config import dp
from aiogram import Bot, Dispatcher
from config import biz_haqimizda, nega_aynan_biz, boglanish_buxoro, boglanish_navoiy ,bizning_manzil
from Data_base import user
from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests

# Ibn Sino salomatlik markazi
API_Key = "6479301334:AAEFdFCkdpnRN4KpMWt0nLXVQLToIKLOPBA"
storage = MemoryStorage()
bot = Bot(token=API_Key)
dp = Dispatcher(bot, storage=storage)


# States
class NewTemplate(StatesGroup):
    city = State()
    muolaja_turi = State()
    time = State()
    full_name = State()
    birthday = State()
    phone_number = State()


# Buttons list
buttonslist = ['🏥 Biz haqimizda', "📞 Biz bilan bog'lanish", '❔ Nega aynan biz', '📍 Bizning manzil', "Doktor ko'rigiga yozilish", "Muolaja haqida malumot", "Parhez haqida malumotlar",
          'Narxlar']
kb = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
button_list = [types.reply_keyboard.KeyboardButton(text=x) for x in buttonslist]

kb.add(*button_list)

kb_manzil = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
lokatsiyalist = [types.reply_keyboard.KeyboardButton('Buxorodagi lokatsiya'),
                 types.reply_keyboard.KeyboardButton('Navoiydagi lokatsiya')]

kb_manzil.add(*lokatsiyalist)



ID = '1107759940'
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if str(message.from_user.id) in user.user_number():
        print('This is old user')
    else:
        tg_id = message.from_user.id
        username = message.from_user.full_name
        # dd/mm/YY H:M:S
        now = datetime.now()
        created_at = now.strftime("%d/%m/%Y %H:%M:%S")


        try:
            user.add(tg_id, username,created_at)
            print('New member added to the database')
        except:
            print('Member already exists in the database')

    await message.reply(text='Ibn Sino salomatlik markazi', reply_markup=kb)



@dp.message_handler(filters.Text(contains='🏥 Biz haqimizda'))
async def about_us(message: types.Message):
    path = f'/home/bahrom/Desktop/TelegramBots/ibnsino/ibnsino_bot/ibnsino.jpg'
    path = open(file=path, mode='rb')
    template = types.InputFile(path)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=template,
        reply_markup=kb,
        caption=biz_haqimizda)


@dp.message_handler(filters.Text(contains="📞 Biz bilan bog'lanish"))
async def contact(message: types.Message):
    await message.reply(
        reply_markup=kb_manzil,
        text='🌆 Shaxarni tanlang')
    


@dp.message_handler(filters.Text(contains="Doktor ko'rigiga yozilish"))
async def contact(message: types.Message):
    await NewTemplate.city.set()
    await message.reply(
        text='🌆 Shaxarni tanlang')
    

@dp.message_handler(state=NewTemplate.city)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await message.answer('Muolaja turini yozing')
    await NewTemplate.next()

@dp.message_handler(state=NewTemplate.muolaja_turi)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['muolaja_turi'] = message.text
    await message.answer('Bormoqchi bolgan qulay vaqtingizni kiriting')
    await NewTemplate.next()


@dp.message_handler(state=NewTemplate.time)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    await message.answer("To'liq ismingizni kiriting")
    await NewTemplate.next()

@dp.message_handler(state=NewTemplate.full_name)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text
    await message.answer("Tug'ilgan kuningizni kiriting")
    await NewTemplate.next()


@dp.message_handler(state=NewTemplate.birthday)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['birthday'] = message.text
    await message.answer('Telefon raqamingizni kiriting')
    await NewTemplate.next()

@dp.message_handler(state=NewTemplate.phone_number)
async def create_template(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    # data base
    id = message.from_user.id
    user.muolaja(state, data['city'], data['muolaja_turi'], data['time'], data['full_name'], data['birthday'], data['phone_number'], id)
    await message.answer("Siz shifokor ko'rigiga yozildingiz", reply_markup=kb)

    chat_id = '1107759940'
    api_token = API_Key  # Replace with your Telegram bot API token

    city = data['city']
    muolaja_turi = data['muolaja_turi']
    time = data['time']
    full_name = data['full_name']
    birthday = data['birthday']
    phone_number = data['phone_number']
    text = f"Shahar: {city}\nMuolaja turi: {muolaja_turi}\nVaqt: {time}\nIsmi: {full_name}\nTug'ilgan kuni: {birthday}\nTelefon raqami: {phone_number}"

    
    api_url = f"https://api.telegram.org/bot{api_token}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    
    response = requests.post(api_url, json=payload)


    await state.finish()




@dp.message_handler(filters.Text(contains="Buxorodagi lokatsiya"))
async def contact(message: types.Message):
    await message.reply(reply_markup=kb, text=boglanish_buxoro)
    

@dp.message_handler(filters.Text(contains="Navoiydagi lokatsiya"))
async def contact(message: types.Message):
    await message.reply(reply_markup=kb, text=boglanish_navoiy)
    


@dp.message_handler(filters.Text(contains="❔ Nega aynan biz"))
async def contact(message: types.Message):
    path = f'/home/bahrom/Desktop/TelegramBots/ibnsino/ibnsino_bot/nega_aynan_biz.jpg'
    path = open(file=path, mode='rb')
    template = types.InputFile(path)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=template,
        reply_markup=kb,
        caption=nega_aynan_biz)
    

@dp.message_handler(filters.Text(contains='📍 Bizning manzil'))
async def about_us(message: types.Message):
    # path = f'/home/bahrom/Desktop/TelegramBots/ibnsino/ibnsino_bot/manzil.jpg'
    # path = open(file=path, mode='rb')
    # template = types.InputFile(path)
    await message.answer(reply_markup=kb, text=bizning_manzil)
    
    # longitude = 69.2085711,15
    # latitude = 41.3334555
    # await bot.send_location(chat_id=message.from_user.id, 
    #     latitude=latitude, 
    #     longitude=longitude)




async def on_startup(_):
    print('Bot is online')
    # user.sql_start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
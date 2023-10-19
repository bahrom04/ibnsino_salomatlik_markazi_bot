from aiogram import types, filters
from config import dp, bot, biz_haqimizda, nega_aynan_biz, boglanish
from Data_base import user
from keyboard.keyboards import kb
from datetime import datetime


# ID = '1107759940'
# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     if str(message.from_user.id) in user.user_number():
#         print('This is old user')
#     else:
#         tg_id = message.from_user.id
#         username = message.from_user.full_name
#         # dd/mm/YY H:M:S
#         now = datetime.now()
#         created_at = now.strftime("%d/%m/%Y %H:%M:%S")


#         try:
#             user.add(tg_id, username)
#             print('New member added to the database')
#         except:
#             print('Member already exists in the database')

#     await message.reply(text='Ibn Sino salomatlik markazi', reply_markup=kb)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
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
    path = f'/home/bahrom/Desktop/TelegramBots/ibnsino/ibnsino_bot/ibnsino.jpg'
    path = open(file=path, mode='rb')
    template = types.InputFile(path)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=template,
        reply_markup=kb,
        caption=boglanish)



@dp.message_handler(filters.Text(contains="❔ Nega aynan biz"))
async def contact(message: types.Message):
    path = f'/home/bahrom/Desktop/TelegramBots/ibnsino/ibnsino_bot/ibnsino.jpg'
    path = open(file=path, mode='rb')
    template = types.InputFile(path)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=template,
        reply_markup=kb,
        caption=nega_aynan_biz)








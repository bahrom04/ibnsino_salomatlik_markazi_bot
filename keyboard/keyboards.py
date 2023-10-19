from aiogram import types


# Buttons list
buttonslist = ['🏥 Biz haqimizda', "📞 Biz bilan bog'lanish", '❔ Nega aynan biz', 'Bizning manzil', "Doktor ko'rigiga yozilish", "Muolaja haqida malumot", "Parhez haqida malumotlar",
          'Narxlar']
kb = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list = [types.reply_keyboard.KeyboardButton(text=x) for x in buttonslist]

kb.add(*button_list)


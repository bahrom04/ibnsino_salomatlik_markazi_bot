import logging
from aiogram import Bot, Dispatcher

# Ibn Sino salomatlik markazi
API_Key = "6479301334:AAEFdFCkdpnRN4KpMWt0nLXVQLToIKLOPBA"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_Key)
dp = Dispatcher(bot)

biz_haqimizda = '''
🏥 Biz haqimizda

📅 Ibn Sino salomatlik markaziga 2015 yilda Dr. Ruslan Rustamovich tomonidan asos solingan

💊 Ibn Sino salomatlik markazi Gijja kasalliklarini aniqlash va ularni davolashga ixtisoslashgan bo'lib
eng so'ngi zamonaviy tashxis va davo uslublarini xalq tabobati bilan uyg'unlashtirgan 

👤 Ibn Sino salomatlik markazi xozirgi kungacha 15 mingdan ortiq bemorni samarali davolagan
    
'''

nega_aynan_biz = '''
❓ Nega aynan biz

🕔 8 yillik tajriba vs vaqt bilan isbotlangan samarali medetsina.

🥼 O'z ishida mutaxasis shifokorlar. Shu bilan birga Respublikamizdagi eng yaxshi shifokor va tabiblar xizmatingizda

💻 Eng so'ngi texnalogiya va yuqori servis, zamonaviy meditsina va xalq tabobati uyg'unligi, yuqori servis va qulay lokatsiya

✅ 18 000 dan ortiq mamnun bemorlar

❤️ Bizning eng muhim vazifamiz bemorlarimizning qulayligini taminlash va ularnig ishonchini oqlash.
'''

boglanish_buxoro = '''
☎️ Aloqa markazi: 95 777 03 03
☎️ Aloqa markazi: 95 600 03 56   

⚡️ Instagram: https://instagram.com/ibnsino_salomatlik_markazi?igshid=MzRlODBiNWFlZA==

📢 Telegram: @ibnsino2015 
📢 Telegram guruhimiz: t.me/ibnsinobuxoro 
🧑‍💻 Telegram bot: @ibnsino_salomatlik_markazi_bot

📍 Bizning manzil:  BUXORO SHAHAR 5 - KICHIK NOHIYA MIRXAN RESTORANI YON TOMONIDA

📍 Lokatsiya: https://www.google.com/maps/place/39%C2%B044'49.9%22N+64%C2%B024'08.7%22E/@39.7471808,64.4022171,105m/data=!3m1!1e3!4m4!3m3!8m2!3d39.7472!4d64.402427?entry=ttu
'''

boglanish_navoiy = '''
☎️ Aloqa markazi: 95 077 03 03  

⚡️ Instagram: https://instagram.com/ibnsino_salomatlik_markazi?igshid=MzRlODBiNWFlZA==

📢 Telegram: @ibnsino2015 
📢 Telegram guruhimiz: t.me/ibnsinobuxoro 
🧑‍💻 Telegram bot: @ibnsino_salomatlik_markazi_bot

📍 Bizning manzil: NAVOIY VILOYAT KARMANA TUMAN OLMOS RESTORANI RO'PARASIDA

📍 Lokatsiya: https://goo.gl/maps/32t95BGwmEgMQfrh6
'''

bizning_manzil = '''
BUXORO

📍 Bizning manzil: BUXORO SHAHAR 5 - KICHIK NOHIYA MIRXAN RESTORANI YON TOMONIDA
📍 Lokatsiya: https://maps.google.com/maps?q=39.747200,64.402427&ll=39.747200,64.402427&z=16


NAVOIY
📍 : NAVOIY VILOYAT KARMANA TUMAN OLMOS RESTORANIRO'PARASIDA
📍 LOKATSYA https://goo.gl/maps/32t95BGwmEgMQfrh6
'''


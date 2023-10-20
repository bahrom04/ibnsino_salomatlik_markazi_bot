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

👤 Ibn Sino salomatlik markazi xozirgi kungacha 18 mingdan ortiq bemorni samarali davolagan
    
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
☎️ Aloqa markazi: 957770303
☎️ Aloqa markazi: 956000356   

📍 Bizning manzil:  BUXORO SHAHAR 5 - KICHIK NOHIYA MIRXAN RESTORANI YON TOMONIDA

'''


boglanish_navoiy = '''
☎️ Aloqa markazi: 950770303  

📍 Bizning manzil: NAVOIY VILOYAT KARMANA TUMAN OLMOS RESTORANI RO'PARASIDA

'''

muolaja_haqida = '''
💊 Ibn Sino salomolatlik markazi gijja kasalliklarini aniqlash va
davolashga ixtisoslashgan bo'lib xozirgi kungacha 
18 mingdan ortiq bemorga xizmat ko'rsatib kelmoqda

💯 Ibn Sino salomatlik markazining boshqa klinikalargan 
farqi va ustunlik tomoni shundaki muolaja 100 % tabiy uslubda 
olib boriladi.Bu esa bemorning biror azolariga zarar yetkazmasdan 
davolash imkoniyati beradi

📅 Davolash muddati qulay, 5 kunni tashkil qilib 
1 kunda 1-1,5 soat vaqtni
'''

ijtimoiy_tarmoqlar = '''
⚡️ Instagram: https://instagram.com/ibnsino_salomatlik_markazi?igshid=MzRlODBiNWFlZA==

📢 Telegram: @ibnsino2015 
📢 Telegram guruhimiz: t.me/ibnsinobuxoro 
🧑‍💻 Telegram bot: @ibnsino_salomatlik_markazi_bot
'''
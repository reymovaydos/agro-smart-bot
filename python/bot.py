import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hbold, hitalic

# --- KONFIGURATSIYA ---
TOKEN = "8248735340:AAEt8k45eMklEkQRkcsWKqfc9WDZXLtPSvw"

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- TUGMALAR ---
def get_main_menu():
    buttons = [
        [KeyboardButton(text="🌿 Biz haqimizda"), KeyboardButton(text="💡 Bizning yechimlar")],
        [KeyboardButton(text="⚙️ Texnologiya qanday ishlaydi?"), KeyboardButton(text="🛠 Zarur uskunalar")],
        [KeyboardButton(text="📊 Bozor imkoniyatlari"), KeyboardButton(text="🤝 Aloqaventures")],
        [KeyboardButton(text="📞 Bog'lanish")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- HANDLERLAR ---

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum! {hbold('AgroSmartCompany')} tizimiga xush kelibsiz.\n"
        f"Biz qishloq xo'jaligini {hitalic('E-Farming Innovation')} orqali transformatsiya qilamiz.",
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )

@dp.message(F.text == "🛠 Zarur uskunalar")
async def tools_handler(message: types.Message):
    """Hujjatdagi datchik va analiz talablariga asoslangan uskunalar bo'limi"""
    text = (
        f"🛠 {hbold('Aqlli dehqonchilik uchun zarur uskunalar:')}\n\n"
        f"1️⃣ {hbold('Aqlli tuproq datchiklari (Sensors)')}: Tuproq namligi, harorati va tarkibidagi minerallarni real vaqtda o'lchaydi.\n"
        f"2️⃣ {hbold('Meteorologik stansiya')}: Ob-havo prognozi va mikroiqlimni tahlil qilish uchun.\n"
        f"3️⃣ {hbold('IoT Gateway')}: Datchiklardan olingan ma'lumotlarni bulutli serverga uzatuvchi qurilma.\n"
        f"4️⃣ {hbold('Avtomatlashtirilgan sugorish tizimi')}: Tizim buyrug'iga binoan suv va ozuqa berishni boshqaradi[cite: 15].\n"
        f"5️⃣ {hbold('Smart Drone')}: Maydon ustidan uchib, vegetatsiya holatini (NDVI indeksi) monitoring qiladi."
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "🌿 Biz haqimizda")
async def about(message: types.Message):
    text = (
        f"🏢 {hbold('AgroSmartCompany')}\n"
        f"Barqaror smart dehqonchilikdagi texnologik yutuq[cite: 2].\n"
        f"Sayt: www.agrohelp.uz [cite: 4]"
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "💡 Bizning yechimlar")
async def solutions(message: types.Message):
    text = (
        f"💡 {hbold('Bizning yechim (Value Proposition)')}:\n\n"
        f"• {hbold('Data-driven ekish')}: Tuproq datchiklari va sun'iy yo'ldosh ma'lumotlari.\n"
        f"• {hbold('Hosilni tezlashtirish')}: Vegetatsiya davrini 15-20 kunga qisqartirish.\n"
        f"• {hbold('Avtomatlashtirilgan nazorat')}: Mobil ilova orqali monitoring."
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "⚙️ Texnologiya qanday ishlaydi?")
async def how_it_works(message: types.Message):
    text = (
        f"⚙️ {hbold('Texnologiya ishlash tartibi')}:\n\n"
        f"🔍 {hbold('Analiz')}: Tuproq va ob-havo tahlili.\n"
        f"📱 {hbold('Tavsiya')}: Ekish vaqti haqida bildirishnoma.\n"
        f"🧪 {hbold('Stimulyatsiya')}: Ozuqa berish ko'rsatmalari.\n"
        f"📈 {hbold('Natija')}: Kam resurs, ko'p hosil."
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "📊 Bozor imkoniyatlari")
async def market(message: types.Message):
    text = (
        f"📊 {hbold('Bozor hajmi')}[cite: 18]:\n\n"
        f"• O'zbekiston QX sektori: {hbold('$20 mlrd+')}.\n"
        f"• Agrotech o'sishi: yiliga {hbold('15%')}.\n"
        f"• Maqsad: 500 ta klaster va 5000 ta fermer."
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "🤝 Aloqaventures")
async def partner(message: types.Message):
    text = (
        f"🤝 {hbold('Nima uchun Aloqaventures?')}:\n\n"
        f"🚀 {hbold('Masshtablash')}: Respublika bo'ylab joriy etish.\n"
        f"💳 {hbold('Integratsiya')}: Aloqabank mijozlariga raqamli xizmatlar."
    )
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "📞 Bog'lanish")
async def contact(message: types.Message):
    await message.answer(f"Murojaat uchun: @reymovaydos \nSayt: www.agrohelp.uz \n Email: reymovaydos03@gmail.com")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
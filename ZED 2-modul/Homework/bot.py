import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

main = KeyboardButton("π Bosh menyu")
contact = KeyboardButton("π Kontaktni ulashish", request_contact=True)
location = KeyboardButton("π Joylashuvni ulashish", request_location=True)
back = KeyboardButton("π Ortga")
Key = ReplyKeyboardMarkup(resize_keyboard=True).add(contact).add(main, back)
menu = ReplyKeyboardMarkup(resize_keyboard=True).add(contact, location)

milliy = KeyboardButton("πΊπΏ Milliy Taomlar")
fast = KeyboardButton("π­ Fast Food")
water = KeyboardButton("πΎ Ichimliklar")
foodsKey = ReplyKeyboardMarkup(resize_keyboard=True).add(milliy, water).add(fast)

palov = InlineKeyboardButton("Osh", callback_data="palov")
lagmon = InlineKeyboardButton("Lag'mon", callback_data="lagman")
milliyKey = InlineKeyboardMarkup().add(palov, lagmon)

cola = InlineKeyboardButton("Coka Cola", callback_data="cola")
pepsi = InlineKeyboardButton("Pepsi", callback_data="pepsi")
waterKey = InlineKeyboardMarkup().add(cola, pepsi)

hotdog = InlineKeyboardButton("Hot Dog", callback_data="hotdog")
hamburger = InlineKeyboardButton("Hamburger", callback_data="hamburger")
fastKey = InlineKeyboardMarkup().add(hotdog, hamburger)

API_TOKEN = '5472551030:AAFG7VFa7N7MBiVgHVSRYPy9sJL5FDGp7r0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom", reply_markup=foodsKey)

@dp.message_handler(text="π Ortga")
async def back(message: types.Message):
    await message.reply("π Ortga", reply_markup=foodsKey)

@dp.message_handler(text="π Bosh menyu")
async def back(message: types.Message):
    await message.reply("π Bosh menyu", reply_markup=foodsKey)

@dp.message_handler(text="πΊπΏ Milliy Taomlar")
async def milliy(message: types.Message):
    await message.reply("Milliy taomlardan birini tanlang: ", reply_markup=milliyKey)

@dp.message_handler(text="π­ Fast Food")
async def fastfood(message: types.Message):
    await message.reply("Fast Food taomlardan birini tanlang: ", reply_markup=fastKey)

@dp.message_handler(text="πΎ Ichimliklar")
async def water(message: types.Message):
    await message.reply("Ichimliklardan birini tanlang: ", reply_markup=waterKey)

@dp.message_handler(content_types="contact")
async def contact(message: types.Message):
    await message.reply("Kontakt qubul qilindi. Siz bilan tez orada operatr bog'lanadi.", reply_markup=foodsKey)

@dp.message_handler(content_types="locatsion")
async def locat(message: types.Message):
    await message.reply("Joylashuv qabul qilindi. Tez orada buyurtmangiz yetqazib beriladi.", reply_markup=foodsKey)

@dp.callback_query_handler(text=["pepsi", "cola", "palov"])
async def echos(call: CallbackQuery):
    await call.message.answer_photo(photo=open(f"img/{call.data}.png", 'rb'), caption=f"Siz {call.data}ni buyurtma bermoqchisiz.", reply_markup=menu)
    await call.answer(cache_time=5)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)

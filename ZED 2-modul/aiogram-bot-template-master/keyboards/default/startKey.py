from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

milliy = KeyboardButton("πΊπΏ Milliy Taomlar")
fast = KeyboardButton("π­ Fast Food")
water = KeyboardButton("πΎ Ichimliklar")
foodsKey = ReplyKeyboardMarkup(resize_keyboard=True).add(milliy, water).add(fast)
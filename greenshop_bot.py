import telebot
from telebot import types

# вставьте сюда токен от BotFather
TOKEN = "8159079607:AAE-mBP-GZPH1Ib31DIvu2MKvLAWzHkIRiA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📦 Каталог")
    btn2 = types.KeyboardButton("ℹ️ О нас")
    btn3 = types.KeyboardButton("📞 Контакты")
    markup.add(btn1, btn2, btn3)
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в GreenShop 🌿\nВыберите раздел:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📦 Каталог":
        bot.send_message(
            message.chat.id,
            "Наш каталог:\n🌱 Растение A — 100₴\n🌵 Растение B — 150₴"
        )
    elif message.text == "ℹ️ О нас":
        bot.send_message(
            message.chat.id,
            "GreenShop 🌿 — магазин растений и аксессуаров."
        )
    elif message.text == "📞 Контакты":
        bot.send_message(
            message.chat.id,
            "Напишите нам: @ваш_контакт\nТелефон: +380XXXXXXXXX"
        )
    else:
        bot.send_message(message.chat.id, f"Вы написали: {message.text}")

print("Бот GreenShop запущен...")
bot.polling(none_stop=True)
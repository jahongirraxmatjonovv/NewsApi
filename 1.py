import requests
import telebot

# Telegram botining tokeni
TOKEN = '6962260840:AAG9qB9ZNcNb9KkCnNrYw0eZkCRiWcqB2CY'

# Bot obyektini yaratamiz
bot = telebot.TeleBot(TOKEN)
def get_name_info(name):
    url = f'https://u12884.xvest5.ru/AvtoApi/api/ismap/ismap.php?ism={name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# /ism buyrug'iga javob berish
@bot.message_handler(commands=['ism'])
def ask_name(message):
    # Foydalanuvchidan ismni so'raymiz
    bot.send_message(message.chat.id, "Ismingizni kiriting:")
    bot.register_next_step_handler(message, send_name_info)

# Foydalanuvchi ismini qabul qilish va ma'lumotlarni jo'natish
def send_name_info(message):
    name = message.text
    name_info = get_name_info(name)
    if name_info:
        # Ma'lumotlar JSON formatida kelganidan, kerakli ma'lumotlarni ajratib olamiz
        mano = name_info.get('mano')
        rasm = name_info.get('rasm')

        # Foydalanuvchiga javob yuboramiz
        if mano:
            with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        # Rasmni yuborish
        bot.send_photo(message.chat.id, open(file_path, 'rb'), caption=name)
    else:
        bot.send_message(message.chat.id, "Ism kiritilmadi. Iltimos, ismingizni yuboring.")
            response = f"Ism ma'nosi: {mano}\n"
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "Ism ma'lumoti topilmadi.")

        # Rasmni yuboramiz
        if rasm:
            bot.send_photo(message.chat.id, rasm)
    else:
        bot.send_message(message.chat.id, "Ism ma'lumoti topilmadi.")

# Botni ishga tushurish
bot.polling()
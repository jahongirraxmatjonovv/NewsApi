import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


BOT_TOKEN = '6962260840:AAGaKAlYWBflztKPJSUBzEX7zMAv2Q4Ix3s'
bot = telebot.TeleBot(BOT_TOKEN)
URL = 'https://b3ae-2605-6440-4013-5-7101-6ab2-5e7f-52d7.ngrok.io/bot/'

def home(request):
    return HttpResponse('bosh.. sahifa')


@csrf_exempt
def bot_view(request):
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
    return HttpResponse(status=200)


def get_news(api_key):
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + api_key
    response = requests.get(url)
    data = response.json()
    return data

# Email yuborish
def send_email(receiver_email, subject, message):
    sender_email = "jahongirraxmatjonov18@gmail.com"
    sender_password = "wpsj zier fwwc yrla"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Yangiliklarni emailga yuborish
def send_news(message):
    email = message.text
    api_key = '2b56b06646a24a3cb2a348b3a109c661'
    news = get_news(api_key)

    for article in news['articles']:
        title = article['title']
        description = article['description']
        url = article['url']
        content = f"{title}\n{description}\nRead more: {url}"
        
        send_email(email, 'Latest News', content)
    
    bot.send_message(message.chat.id, "Yangiliklar elektron manzilga yuborildi!")


# Email so'rab, yangiliklarni olish
@bot.message_handler(commands=['start'])
def request_email(message):
    msg = bot.send_message(message.chat.id, "Iltimos, elektron manzilingizni kiriting:")
    bot.register_next_step_handler(msg, send_news)
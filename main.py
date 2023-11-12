import telebot
import requests

TOKEN = '5021398357:AAE62C4x-jptJ3S2gLpuHvrXru6xM5yIAaQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Song Download Bot! Just send me the name of the song you want to download.")

@bot.message_handler(func=lambda message: True)
def download_song(message):
    song_name = message.text
    download_url = f'https://api.example.com/download?song={song_name}'
    response = requests.get(download_url)
    if response.status_code == 200:
        bot.send_audio(message.chat.id, response.content)
    else:
        bot.reply_to(message, "Sorry, I couldn't find the song you requested.")

bot.polling()

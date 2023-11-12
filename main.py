import telebot
from pytube import YouTube

# Telegram Bot Token
TOKEN = '5021398357:AAE62C4x-jptJ3S2gLpuHvrXru6xM5yIAaQ'

# Initialize Telegram Bot
bot = telebot.TeleBot(TOKEN)

# Handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to the YouTube Song Downloader Bot!')

# Handler for /download command
@bot.message_handler(commands=['download'])
def download_song(message):
    # Get the YouTube video URL from the message
    url = message.text.split(' ')[1]

    try:
        # Download the YouTube video
        video = YouTube(url)
        audio = video.streams.filter(only_audio=True).first()
        audio.download()

        bot.reply_to(message, 'Song downloaded successfully!')
    except Exception as e:
        bot.reply_to(message, f'Error: {str(e)}')

# Start the Telegram Bot
bot.polling()

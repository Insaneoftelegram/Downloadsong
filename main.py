import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('5021398357:AAE62C4x-jptJ3S2gLpuHvrXru6xM5yIAaQ')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if "/song" in message.text:
        # Process the song request
        process_song_request(message)
    else:
        # Send a reminder to include '/song' in the message
        bot.reply_to(message, "Please include '/song song_name ' in your message.")

def process_song_request(message):
    # Process the song request here
    bot.reply_to(message, "Thank you for your song request!")

bot.polling()

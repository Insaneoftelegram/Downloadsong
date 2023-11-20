import telebot
import requests
import os

# Initialize the Telegram bot
bot = telebot.TeleBot('5021398357:AAE62C4x-jptJ3S2gLpuHvrXru6xM5yIAa')

# Define the command to handle song downloads
@bot.message_handler(commands=['download'])
def handle_download(message):
    # Get the song name from the user's message
    song_name = message.text.split(' ', 1)[1]

    # Search for the song on a music API
    api_url = f'https://2a230af10e0a40638dc77c1febb47170.spotify.com/search?q={song_name}'
    response = requests.get(api_url)
    song_data = response.json()

    # Check if any songs were found
    if song_data['total_results'] > 0:
        # Get the first song from the search results
        first_song = song_data['results'][0]

        # Download the song
        song_url = first_song['url']
        song_file = requests.get(song_url)
        with open(f'{song_name}.mp3', 'wb') as file:
            file.write(song_file.content)

        # Apply the auto filter to the downloaded song
        os.system(f'ffmpeg -i {song_name}.mp3 -af "equalizer=f=1000:width_type=h:width=200:g=10" {song_name}_filtered.mp3')

        # Send the filtered song to the user
        bot.send_audio(message.chat.id, open(f'{song_name}_filtered.mp3', 'rb'))

    else:
        bot.reply_to(message, 'No songs found.')

# Start the bot
bot.polling()

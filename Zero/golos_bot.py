import telebot
import pyttsx3

# Токен вашего бота
TOKEN = '7436010539:AAE2o8DuP00CaOEDSidHtOj7O5vZvd0t-pI'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Функция для обработки входящих сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Озвучиваем текст сообщения
    engine = pyttsx3.init()
    engine.save_to_file(message.text, 'message.mp3')
    engine.runAndWait()
    
    # Отправляем голосовое сообщение пользователю
    with open('message.mp3', 'rb') as voice:
        bot.send_voice(message.chat.id, voice)

# Запускаем бота
bot.polling()
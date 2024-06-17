import telebot

# Замените 'YOUR_BOT_TOKEN_HERE' на токен вашего бота
API_TOKEN = '7436010539:AAE2o8DuP00CaOEDSidHtOj7O5vZvd0t-pI'

# Создаем экземпляр бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ваш Телеграм бот.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я могу ответить на ваши сообщения. Просто напишите мне что-нибудь!")

# Обработчик для сообщения "привет"
@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def greet_user(message):
    bot.reply_to(message, "Привет! Как я могу помочь вам сегодня?")

# Обработчик для сообщения "как дела"
@bot.message_handler(func=lambda message: message.text.lower() == "как дела")
def ask_status(message):
    bot.reply_to(message, "Все отлично! Спасибо, что спросили. Как у вас дела?")

# Обработчик для всех остальных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю это сообщение. Попробуйте написать 'привет' или 'как дела'.")

# Запуск бота
bot.polling()
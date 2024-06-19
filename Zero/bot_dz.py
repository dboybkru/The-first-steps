import telebot
from telebot import types

API_TOKEN = '7436010539:AAE2o8DuP00CaOEDSidHtOj7O5vZvd0t-pI'

bot = telebot.TeleBot(API_TOKEN)

# Глобальные переменные для подсчета обращений
session_counts = {}
total_requests = 0

# Функции для удаления гласных и согласных (русские и английские буквы)
def remove_vowels(message):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return ''.join([char for char in message if char not in vowels])

def remove_consonants(message):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    return ''.join([char for char in message if char not in consonants])

# Функция для подсчета символов
def count_characters(message):
    return len(message)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ваш бот для помощи. Используйте команду /help для получения списка команд.")
    session_counts[message.chat.id] = 0

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Список доступных команд:\n"
        "/start - Начать работу с ботом\n"
        "/help - Получить список команд\n"
        "/reverse - Перевернуть текст\n"
        "/caps - Преобразовать текст в заглавные буквы\n"
        "/remove_vowels - Удалить гласные буквы из текста\n"
        "/remove_consonants - Удалить согласные буквы из текста\n"
        "/count_chars - Подсчитать количество символов в тексте"
    )
    bot.reply_to(message, help_text)

# Обработчики команд для запроса текста
@bot.message_handler(commands=['reverse', 'caps', 'remove_vowels', 'remove_consonants', 'count_chars'])
def handle_command(message):
    command = message.text.split()[0][1:]
    bot.send_message(message.chat.id, f"Пожалуйста, отправьте текст для команды /{command}.")
    bot.register_next_step_handler(message, process_text, command)

def process_text(message, command):
    global total_requests
    total_requests += 1
    session_counts[message.chat.id] = session_counts.get(message.chat.id, 0) + 1

    text = message.text
    response = ""

    if command == 'reverse':
        response = text[::-1]
    elif command == 'caps':
        response = text.upper()
    elif command == 'remove_vowels':
        response = remove_vowels(text)
    elif command == 'remove_consonants':
        response = remove_consonants(text)
    elif command == 'count_chars':
        response = f"Количество символов: {count_characters(text)}"

    response += f"\n\nОбщее количество обращений за сеанс: {session_counts[message.chat.id]}"
    response += f"\nВсего обращений: {total_requests}"
    bot.reply_to(message, response)

# Функция для обработки остальных сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю эту команду. Используйте /help для получения списка команд.")

# Запускаем бота
bot.polling()
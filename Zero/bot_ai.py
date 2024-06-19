import telebot
import openai

# Замените 'YOUR_TELEGRAM_API_KEY' на ваш API ключ Telegram
TELEGRAM_API_KEY = '7436010539:AAE2o8DuP00CaOEDSidHtOj7O5vZvd0t-pI'
# Замените 'YOUR_OPENAI_API_KEY' на ваш API ключ OpenAI
OPENAI_API_KEY = 'sk-VJhW0aBy6VirBefZdFvOIKQjdayw2Lqs'

# Создаем бота
bot = telebot.TeleBot(TELEGRAM_API_KEY)

# Настройка клиента OpenAI
openai.api_key = OPENAI_API_KEY
openai.api_base = "https://api.proxyapi.ru/openai/v1"

# Хранение истории общения для каждого пользователя
user_conversations = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Начни общаться с нейросетью. Введите 'exit' для выхода.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    user_input = message.text

    if user_input.lower() == 'exit':
        bot.reply_to(message, "Чат завершен.")
        return

    if user_id not in user_conversations:
        user_conversations[user_id] = [{"role": "user", "content": "Hello, world"}]  # Начальное сообщение

    user_conversations[user_id].append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            messages=user_conversations[user_id]
        )

        response_message = response.choices[0].message['content']
        bot.reply_to(message, response_message)

        # Добавляем ответ нейросети в историю общения
        user_conversations[user_id].append({"role": "assistant", "content": response_message})

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")

if __name__ == "__main__":
    bot.polling()

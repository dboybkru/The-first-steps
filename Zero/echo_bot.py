import telebot

    # Вставьте свой токен API Telegram
API_TOKEN = '7436010539:AAE2o8DuP00CaOEDSidHtOj7O5vZvd0t-pI'

    # Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

    # Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я эхо-бот. Отправь мне сообщение, и я повторю его!")

    # Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

    # Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
        
"""В этом примере:
- `API_TOKEN` должен быть заменен на ваш реальный токен бота, который можно получить у [BotFather](https://core.telegram.org/bots#botfather) в Telegram.
- `@bot.message_handler(commands=['start'])` задает обработчик для команды `/start`, который отправляет приветственное сообщение.
- `@bot.message_handler(func=lambda message: True)` задает обработчик для всех текстовых сообщений и отправляет обратно тот же текст.

Запустите скрипт, и бот будет готов к работе. Теперь вы можете отправлять ему сообщения, и он будет их повторять.

Пример запуска скрипта:
```sh
python echo_bot.py
```

Этот бот будет работать в режиме постоянного опроса (`polling`), что означает, что он будет непрерывно проверять новые сообщения и обрабатывать их по мере поступления."""
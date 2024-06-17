def convert_seconds(seconds):
    # Количество секунд в одной минуте, часе и дне
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    # Вычисляем количество дней, часов, минут и оставшихся секунд
    days = seconds // SECONDS_IN_DAY
    seconds %= SECONDS_IN_DAY

    hours = seconds // SECONDS_IN_HOUR
    seconds %= SECONDS_IN_HOUR

    minutes = seconds // SECONDS_IN_MINUTE
    seconds %= SECONDS_IN_MINUTE

    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

# Пример использования
input_seconds = int(input("Введите количество секунд: "))
formatted_time = convert_seconds(input_seconds)
print(f"Форматированное время: {formatted_time}")

"""Этот код выполняет следующие шаги:
1. Определяет количество секунд в минуте, часе и дне.
2. Вычисляет количество дней, часов, минут и оставшихся секунд из заданного числа секунд.
3. Возвращает строку в формате "дни:часы:минуты:секунды", где часы, минуты и секунды отображаются с ведущими нулями, если это необходимо (например, 02 вместо 2).
4. Принимает количество секунд от пользователя и выводит отформатированное время.

Пример работы программы:
```
Введите количество секунд: 98765
Форматированное время: 1:03:26:05
```

Таким образом, 98765 секунд преобразуются в 1 день, 3 часа, 26 минут и 5 секунд."""

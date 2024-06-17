from fractions import Fraction

# Данное вещественное число
decimal_number = 14.375

# Преобразование вещественного числа в дробь
fraction = Fraction(decimal_number).limit_denominator()

# Печать результата
print(f"{decimal_number} = {fraction.numerator}/{fraction.denominator}")

"""Этот код выполняет следующие шаги:
1. Импортирует класс `Fraction` из библиотеки `fractions`.
2. Преобразует вещественное число `14.375` в дробь.
3. Использует метод `limit_denominator()` для получения наименьшей обыкновенной дроби, эквивалентной данному вещественному числу.
4. Выводит результат в формате `числитель/знаменатель`.

Когда вы выполните этот код, он выведет:
```
14.375 = 115/8
```

Таким образом, наименьшая обыкновенная дробь, равная 14.375, это 115/8."""
import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

if __name__ == "__main__":
    # Укажите диапазон значений
    min_value = 1
    max_value = 100

    # Генерация случайного числа
    random_number = generate_random_number(min_value, max_value)

    # Вывод случайного числа на экран
    print(f"Случайное число в диапазоне от {min_value} до {max_value}: {random_number}")
    
    
    """Эта программа использует модуль `random` для генерации случайного целого числа в указанном диапазоне (от `min_value` до `max_value` включительно). Вы можете изменить значения `min_value` и `max_value`, чтобы задать другой диапазон.
"""
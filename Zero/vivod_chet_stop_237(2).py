def print_even_until_237(numbers):
    for number in numbers:
        if number == 237:
            print(f"Encountered 237, stopping.")
            break
        if number % 2 == 0:
            print(number)

# Пример использования
numbers_list = [1, 2, 3, 4, 5, 1, 8, 10, 12, 14, 16, 237, 20]  # Задайте здесь ваш список чисел
print_even_until_237(numbers_list)
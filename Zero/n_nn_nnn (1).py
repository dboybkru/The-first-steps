def calculate_expression(n):
    # Преобразуем число в строку, чтобы создать 'nn' и 'nnn'
    n_str = str(n)
    nn = int(n_str * 2)  # 'nn'
    nnn = int(n_str * 3)  # 'nnn'
    
    # Рассчитаем итоговое значение
    result = n + nn + nnn
    return result

# Пример использования
n = int(input("Введите целое число: "))
result = calculate_expression(n)
print(f"Результат выражения {n} + {n}{n} + {n}{n}{n} = {result}")
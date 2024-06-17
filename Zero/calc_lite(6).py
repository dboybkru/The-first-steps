def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль."
    return x / y

def calculator():
    try:
        # Ввод чисел пользователем
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        # Ввод операции пользователем
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        operation = input("Введите номер операции (1/2/3/4): ")
        
        # Вычисление и вывод результата
        if operation == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Ошибка: неверный выбор операции.")
    except ValueError:
        print("Ошибка: введите корректные числа.")

# Запуск калькулятора
calculator()

"""Этот код позволяет пользователю:
1. Ввести два числа.
2. Выбрать операцию из предложенного списка (сложение, вычитание, умножение, деление).
3. Выполняет выбранную операцию и выводит результат.

Если пользователь введет некорректные данные или попытается выполнить деление на ноль, программа выведет соответствующее сообщение об ошибке."""
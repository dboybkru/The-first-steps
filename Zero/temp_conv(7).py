def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    try:
        # Выбор направления перевода
        print("Выберите направление перевода:")
        print("1. Цельсий -> Фаренгейт")
        print("2. Фаренгейт -> Цельсий")
        choice = input("Введите номер выбора (1/2): ")
        
        if choice == '1':
            # Ввод температуры в градусах Цельсия
            celsius = float(input("Введите температуру в градусах Цельсия: "))
            # Перевод в градусы Фаренгейта
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")
        
        elif choice == '2':
            # Ввод температуры в градусах Фаренгейта
            fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
            # Перевод в градусы Цельсия
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} градусов Фаренгейта = {celsius} градусов Цельсия")
        
        else:
            print("Ошибка: неверный выбор.")
    except ValueError:
        print("Ошибка: введите корректное число.")

# Запуск программы
temperature_converter()

"""Этот код позволяет пользователю:
1. Выбрать направление перевода температуры (из Цельсия в Фаренгейт или из Фаренгейта в Цельсий).
2. Ввести температуру в соответствующих единицах.
3. Получить результат перевода температуры.

Если пользователь введет некорректные данные, программа выведет сообщение об ошибке."""
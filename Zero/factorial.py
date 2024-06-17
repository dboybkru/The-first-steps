def factorial(n):
  if n < 0:
      return "Факториал не определён для отрицательных чисел"
  elif n == 0 or n == 1:
      return 1
  else:
      result = 1
      for i in range(2, n + 1):
          result *= i
      return result

# Пример использования:
try:
  number = int(input("Введите число для вычисления факториала: "))
  print(f"Факториал числа {number} равен {factorial(number)}")
except ValueError:
  print("Пожалуйста, введите целое число.")
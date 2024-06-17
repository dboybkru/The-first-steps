def find_most_frequent_number(n, a):
  frequency = {}

  # Подсчет частоты каждого числа
  for num in a:
      if num in frequency:
          frequency[num] += 1
      else:
          frequency[num] = 1

  # Поиск числа с наибольшей частотой
  most_frequent_num = -1
  max_frequency = -1

  for num, freq in frequency.items():
      if freq > max_frequency or (freq == max_frequency and num > most_frequent_num):
          max_frequency = freq
          most_frequent_num = num

  return most_frequent_num

# Ввод данных
n = int(input())
a = list(map(int, input().split()))

# Получение результата и вывод
result = find_most_frequent_number(n, a)
print(result)
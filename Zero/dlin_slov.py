def longest_common_prefix(words):
  if not words:
      return ""

  # Начинаем с первого слова в списке как с общего префикса
  prefix = words[0]

  for word in words[1:]:
      # Пока префикс не найден в начале слова, укорачиваем его
      while word[:len(prefix)] != prefix:
          prefix = prefix[:-1]
          if not prefix:
              return ""

  return prefix

# Пример использования:
words = ["flower", "flow", "flight"]
print("Максимально длинное общее начало:", longest_common_prefix(words))

words = ["dog", "racecar", "car"]
print("Максимально длинное общее начало:", longest_common_prefix(words))
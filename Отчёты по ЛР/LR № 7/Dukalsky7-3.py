text = input("Введите текст: ")
word = input("Введите слово: ")
count = text.count(word)
print(f"Слово '{word}' {'найдено' if word in text else 'не найдено'}, встречается {count} раз")
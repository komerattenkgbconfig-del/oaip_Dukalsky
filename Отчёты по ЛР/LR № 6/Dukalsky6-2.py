text = input("Введите текст: ")
old, new = input("Введите строку1 строку2: ").split(maxsplit=1)
print(f"Результат: {text.replace(old, new)}")
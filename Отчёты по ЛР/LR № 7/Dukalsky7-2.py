password = input("Введите пароль: ")
confirm = input("Подтвердите пароль: ")
if password == confirm:
    auth = input("Введите пароль для авторизации: ")
    print("Access" if auth == password else "Denied")
else:
    print("Пароли не совпадают")
year = int(input("Введите год: "))
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(f"Год {year} {'високосный' if is_leap else 'не високосный'}")
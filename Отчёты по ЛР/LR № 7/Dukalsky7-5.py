import math

parts = input("Введите число1 знак число2: ").split()
if len(parts) == 3:
    try:
        num1, op, num2 = float(parts[0]), parts[1], float(parts[2])
        result = {
            '*': num1 * num2, '+': num1 + num2, '-': num1 - num2,
            '**': num1 ** num2, '%%': num1 * num2 / 100,
            '/': num1 / num2, '%': num1 % num2, '//': num1 // num2,
            '/**': math.sqrt(num1)
        }.get(op, "Неизвестная операция")
        print(f"Результат: {result}")
    except: 
        print("Ошибка вычисления")
else:
    print("Некорректный ввод")
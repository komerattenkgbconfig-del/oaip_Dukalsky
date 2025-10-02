import random
import string

generate_random_string = lambda length: ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') for _ in range(length))

message, n = input("Сообщение: "), int(input("n: "))
encoded = ''.join(char + generate_random_string(n) for char in message)

print(f"Исходное: '{message}'\nЗакодированное: '{encoded}'")
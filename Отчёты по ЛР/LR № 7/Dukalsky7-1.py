direction = input("Введите направление (left/right/straight/back): ")
actions = {"left": "влево", "right": "вправо", "straight": "прямо", "back": "назад"}
print(f"Иду {actions[direction]}" if direction in actions else "Неправильное направление")
import random
import string

# Функція, яка не повертає значення, а лише виводить серійні номери
def generate_serial_numbers():
    for _ in range(10):
        serial = "-".join(
            "".join(random.choices(string.ascii_uppercase, k=4)) for _ in range(3)
        )
        print(serial)

# Функція, яка повертає список серійних номерів, що починаються з літери "Q"
def generate_serial_numbers_starting_with_Q():
    serials_with_q = []
    for _ in range(12):
        serial = "Q" + "-".join(
            "".join(random.choices(string.ascii_uppercase, k=3)) for _ in range(3)
        )
        serials_with_q.append(serial)
    return serials_with_q
vowels = "аеєиіїоуюя"

# Функція для підрахунку голосних у рядку, яка повертає кількість голосних у рядку
def count_vowels_in_line(line):
    return sum(1 for char in line.lower() if char in vowels)

# Функція, яка не повертає значення, а лише виводить кількість голосних у кожному рядку
def count_vowels_in_text(lines):
    for i, line in enumerate(lines, start=1):
        count = count_vowels_in_line(line)
        print(f"Рядок {i}: кількість голосних = {count}")
import math

# Модуль з функціями для обчислення параметрів циліндра

# Функція для обчислення повної площі поверхні циліндра
def full_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Функція для обчислення площі бічної поверхні циліндра
def lateral_surface_area(radius, height):
    return 2 * math.pi * radius * height

# Функція для обчислення об'єму циліндра
def volume_of_cylinder(radius, height):
    return math.pi * radius**2 * height
import modulefinder as cyl_module  # Імпортуємо модуль для циліндра

# Виклик функцій для Завдання 1
generate_serial_numbers()
print(generate_serial_numbers_starting_with_Q())

# Виклик функцій для Завдання 2
lines = [
    "Тут ваш перший рядок тексту",
    "І тут ваш другий рядок тексту"
]
count_vowels_in_text(lines)

# Виклик функцій для Завдання 3
radius = 5
height = 10
print("Повна площа поверхні:", cyl_module.full_surface_area(radius, height))
print("Площа бічної поверхні:", cyl_module.lateral_surface_area(radius, height))
print("Об'єм:", cyl_module.volume_of_cylinder(radius, height))

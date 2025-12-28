import sys
import os


print("--- 'План поиска' модулей (sys.path) ---")

# Просто перебираем список и выводим каждый пункт плана
for index, folder in enumerate(sys.path, start=1):
    print(f"Шаг {index}: Проверить папку '{folder}'")

print("*" * 80)

# Теперь представим, что у нас есть папка /libs на одном уровне с /scripts,
# и в ней лежит модуль custom_math.py, который мы хотим импортировать.
# Но по умолчанию Python не знает о папке /libs, поэтому импорт не сработает.
# Нам нужно добавить путь к /libs в sys.path.

# --- Шаг 1: Формируем путь к папке с библиотеками ---

# __file__ - специальная переменная, хранящая путь к текущему файлу
# os.path.dirname(__file__) - получаем путь к папке, где лежит скрипт (/scripts)
script_folder = os.path.dirname(__file__)

# os.path.dirname(script_folder) - поднимаемся на уровень выше (/project)
project_folder = os.path.dirname(script_folder)

# os.path.join(...) - собираем путь к папке /libs
libs_folder = os.path.join(project_folder, 'libs')


# --- Шаг 2: Добавляем этот путь в sys.path ---

# Проверяем, чтобы не добавить путь несколько раз
if libs_folder not in sys.path:
    print(f"Добавляю в 'план поиска': {libs_folder}")
    sys.path.append(libs_folder)


# --- Шаг 3: Теперь импорт сработает без ошибок! ---

print("Пытаюсь импортировать custom_math...")
# Предполагаем, что в custom_math.py есть функция add
import custom_math
print("Импорт прошел успешно!")


# Теперь можно использовать функции из этого модуля
result = custom_math.add(5, 3)
print(f"Результат работы custom_math.add(5, 3) = {result}")

print("=" * 80)
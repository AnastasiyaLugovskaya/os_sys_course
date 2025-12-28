import sys
import os

print("--- Сравниваем os.name и sys.platform ---")
print(f"os.name говорит:      '{os.name}'")
print(f"sys.platform говорит: '{sys.platform}'")

print("\n--- Пример использования sys.platform для конкретных приветствий ---")

# Используем if/elif/else для проверки конкретной платформы
if sys.platform == 'win32':
    print("Привет, пользователь Windows! Как дела с обновлениями?")
elif sys.platform == 'linux':
    print("Привет, пользователь Linux! Терминал - твой лучший друг.")
elif sys.platform == 'darwin':
    print("Привет, пользователь macOS! Наслаждаешься дизайном?")
else:
    print(f"Ого! Ты используешь интересную систему: {sys.platform}")

print('*' * 80)
print("\n--- Информация для человека (sys.version) ---")
python_version_string = sys.version
print(python_version_string)
print('*' * 80)

print("\n--- Информация для машины (sys.version_info) ---")
version_info = sys.version_info

print(f"Полный объект: {version_info}")
print(f"Мажорная версия (major): {version_info.major} (или version_info[0])")
print(f"Минорная версия (minor): {version_info.minor} (или version_info[1])")
print(f"Патч-версия (micro):  {version_info.micro} (или version_info[2])")
print('*' * 80)

# Наш скрипт требует Python версии 3.6 или выше
REQUIRED_MAJOR = 3
REQUIRED_MINOR = 6

print(f"\nТекущая версия Python: {sys.version_info.major}.{sys.version_info.minor}")
print(f"Требуемая версия: {REQUIRED_MAJOR}.{REQUIRED_MINOR} или выше")

# Проверяем, что мы работаем на Python 3
if sys.version_info.major != REQUIRED_MAJOR:
    print("Ошибка: Этот скрипт работает только на Python 3.")
    # В следующем уроке мы узнаем, как правильно завершать работу
    # sys.exit(1)

# Проверяем, что минорная версия достаточно новая
elif sys.version_info.minor < REQUIRED_MINOR:
    print(f"Ошибка: Требуется Python {REQUIRED_MAJOR}.{REQUIRED_MINOR} или новее.")
    # sys.exit(1)

else:
    print("Отлично! Ваша версия Python подходит.")
    # ... здесь начинается основной код скрипта ...
print('*' * 80)
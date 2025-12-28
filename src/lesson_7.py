import os
import subprocess


# Команда, которую мы хотим передать операционной системе
command_to_run = 'echo Привет из командной строки!'

if __name__ == '__main__':
    # 1. Выполнение команды через os.system()
    print("\n--- Мой Python-скрипт начинает работу. ---")

    print("Сейчас я попрошу ОС выполнить команду...")

    # Передаем команду "джинну"
    os.system(command_to_run)

    print("--- ОС выполнила команду, скрипт продолжает работу. ---")
    print("*" * 80)

    # 2. Выполнение команы через subprocess
    # Пример для Windows: пропинговать google.com 1 раз
    command_win = ['ping', '-n', '1', 'google.com']

    # Пример для Linux/macOS: пропинговать google.com 1 раз
    command_nix = ['ping', '-c', '1', 'google.com']
    print("*" * 80)

    # Запускаем команду (выберите нужную для вашей ОС)
    print("\n--- Запускаем ping через subprocess ---")
    subprocess.run(command_win)

    # 3. Выполение встроенных команд Windows
    # ПРАВИЛЬНЫЙ способ для встроенных команд Windows
    command_as_list = ['cmd', '/c', 'dir']

    # Запускаем команду
    result = subprocess.run(command_as_list, capture_output=True, text=True, encoding='cp866')
    # Теперь вся информация у нас в объекте result
    print(f"\nКоманда завершилась с кодом: {result.returncode}")  # 0 - значит "успех"

    print("\n--- Вывод команды (stdout): ---")
    print(result.stdout)

    # Мы можем работать с выводом как с обычной строкой!
    file_count = len(result.stdout.splitlines())
    print(f"\nНайдено объектов: {file_count}")
    print("*" * 80)
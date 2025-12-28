import os

# Наши "точки назначения"
folder = 'data'
subfolder = 'images'
filename = 'profile.jpg'

# Создадим примеры путей для разных ОС
path_windows = r'C:\Users\Admin\Documents\project\main.py' # r'' - "сырая" строка, чтобы \ не экранировался
path_linux = '/home/user/documents/project/main.py'

source_path = '/home/user/downloads/data.csv'
archive_dir = '/home/user/archive'

current_file_path = '/path/to/my/script.py'

path_to_dir = 'test_directory'
path_to_file = 'test_file.txt'

if __name__ == "__main__":

    # 1. Объединение пути к файлу при помощи os.path.join
    print("\nПрокладываю маршрут с помощью os.path.join()...")

    # Передаем точки навигатору
    full_path = os.path.join(folder, subfolder, filename)

    # Смотрим, какой маршрут он построил
    print(f"Идеальный путь для этой системы: {full_path}")
    print("*" * 80)

    # 2. Получение имени файла из пути через os.path.basename()
    print("\n--- Использую os.path.basename() ---")

    # Применяем к пути в стиле Windows
    filename_win = os.path.basename(path_windows)
    print(f"Имя файла из пути Windows: {filename_win}")

    # Применяем к пути в стиле Linux
    filename_lin = os.path.basename(path_linux)
    print(f"Имя файла из пути Linux: {filename_lin}")
    print("*" * 80)

    # 3. Получение пути к папке и имени файла через os.path.split()
    print("\n--- Использую os.path.split() ---")

    # Разделяем путь
    path_parts = os.path.split(path_linux)
    print(f"Результат (кортеж из 2-х частей): {path_parts}")

    # Самый удобный способ - сразу разложить результат в две переменные
    directory_path, file_name = os.path.split(path_linux)

    print(f"Путь к папке: {directory_path}")
    print(f"Имя файла:    {file_name}")
    print("*" * 80)

    # 4. Перемещение файла в новую директорию
    # Получаем только имя файла
    filename = os.path.basename(source_path)  # -> 'data.csv'

    # Собираем новый, правильный путь
    destination_path = os.path.join(archive_dir, filename)  # -> '/home/user/archive/data.csv'

    # os.rename(source_path, destination_path) # Команда для перемещения
    print(f"\nНовый путь: {destination_path}")
    print("*" * 80)

    # 5. Создание пути для нового файла в текущей директории
    # Получаем путь к папке, где лежит наш скрипт
    script_directory, _ = os.path.split(current_file_path)  # Нам не нужно имя файла, используем _

    # Создаем путь для лог-файла в этой папке
    log_file_path = os.path.join(script_directory, 'app.log')  # -> '/path/to/my/app.log'

    print(f"\nЛог-файл будет создан здесь: {log_file_path}")
    print("*" * 80)

    # 6. Проверка является ли переданный путь файлом или директорией
    # Подготовим среду: создадим папку для теста
    os.makedirs('test_directory', exist_ok=True)

    print(f"\n--- Проверяю '{path_to_dir}' с помощью os.path.isdir() ---")

    if os.path.isdir(path_to_dir):
        print(f"✅ Да, '{path_to_dir}' — это директория.")
    else:
        print(f"❌ Нет, '{path_to_dir}' — это не директория.")

    # Уберем за собой
    os.rmdir(path_to_dir)

    # Подготовим среду: создадим файл для теста
    with open('test_file.txt', 'w') as f:
        f.write('test')

    print(f"\n--- Проверяю '{path_to_file}' с помощью os.path.isfile() ---")

    if os.path.isfile(path_to_file):
        print(f"✅ Да, '{path_to_file}' — это файл.")
    else:
        print(f"❌ Нет, '{path_to_file}' — это не файл.")

    # Уберем за собой
    os.remove(path_to_file)

    # 7. Проверка содержимого переданной директории
    print("\n--- Анализирую содержимое текущей директории ---")

    # Получаем список всех имен в текущей папке
    for item_name in os.listdir('.'):
        # Для каждого имени мы проверяем, что это - файл или папка

        if os.path.isdir(item_name):
            print(f"[ПАПКА]  {item_name}")

        elif os.path.isfile(item_name):
            # Если это файл, давайте узнаем его размер!
            file_size = os.stat(item_name).st_size
            print(f"[ФАЙЛ]   {item_name}  (размер: {file_size} байт)")

        else:
            # Это может быть что-то другое, например, символическая ссылка
            print(f"[ДРУГОЕ] {item_name}")

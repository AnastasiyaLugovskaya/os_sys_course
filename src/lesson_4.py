import os

start_path = os.getcwd()

target_folder = 'data'
all_items = os.listdir(target_folder)

new_folder_name = 'results'
path_to_create = 'reports/2025/september'

folder_to_delete = 'temp_folder'
folder_to_delete_not_empty = 'temp_folder_with_file'
deep_path = 'level1/level2/level3'


if __name__ == "__main__":
    # Определение текущей рабочей директории
    print(f"Скрипт запущен в папке: {start_path}")

    print(f"\nЯ нахожусь в: {os.getcwd()}")
    print("Осматриваюсь по сторонам...")
    items_here = os.listdir('.')
    print(f"Здесь я вижу: {items_here}")

    # Просмотр содержимого указанной директории
    print("\nЗаглядываю в папку 'data'...")
    items_in_data = os.listdir('data')
    print(f"В папке 'data' находится: {items_in_data}")

    print(f"\nИщу все .txt файлы в папке '{target_folder}'...")
    for item_name in all_items:
        if item_name.endswith('.txt'):
            print(f"  Найден текстовый файл: {item_name}")
    print("Поиск завершен.")

    print("-" * 80)

    # Создание новой папки, если её нет
    print(f"\nПроверяю, существует ли папка '{new_folder_name}'...")
    if new_folder_name not in os.listdir('.'):
        print(f"Папки нет. Создаю папку '{new_folder_name}'...")
        os.mkdir(new_folder_name)
        print("Папка успешно создана!")
    else:
        print(f"Папка '{new_folder_name}' уже существует.")

    print("-" * 80)

    # Создание вложенной структуры папок
    print(f"\nСобираюсь создать структуру папок: '{path_to_create}'")
    os.makedirs(path_to_create, exist_ok=True)
    print("Структура успешно создана!")

    print("-" * 80)

    # Удаление папки (если она существует)
    os.makedirs(folder_to_delete, exist_ok=True)
    print(f"Папка '{folder_to_delete}' создана.")
    print(f"Пытаюсь удалить ПУСТУЮ папку '{folder_to_delete}'...")
    os.rmdir(folder_to_delete)
    print("Успешно удалено!")

    print("-" * 80)
    # Удаление непустой папки
    os.makedirs(folder_to_delete_not_empty, exist_ok=True)
    with open(os.path.join(folder_to_delete_not_empty, 'temp_file.txt'), 'w', encoding='utf-8') as f:
        f.write("Временный файл.")
    print(f"\nПапка '{folder_to_delete_not_empty}' с файлом создана и содержит файл.")
    print(f"Пытаюсь удалить НЕПУСТУЮ папку '{folder_to_delete_not_empty}'...")
    try:
        os.rmdir(folder_to_delete_not_empty)
    except OSError as e:
        print(f"Ошибка: {e.strerror}. Папка не пуста, удаление невозможно с помощью os.rmdir().")

    print("-" * 80)

    # Удаление глубокой структуры папок
    os.makedirs(deep_path, exist_ok=True)
    print(f"\nСоздана глубокая структура папок: '{deep_path}'")
    print(f"Пытаюсь удалить всю структуру папок '{deep_path}'...")
    os.removedirs(deep_path)
    print("Глубокая структура папок успешно удалена!")

    print("-" * 80)

    # Изменение текущей рабочей директории
    print("\nФайл 'info.txt' лежит в папке 'data'.")
    print("Перехожу в папку 'data'...")
    os.chdir('data')
    new_path = os.getcwd()
    print(f"Теперь я нахожусь в папке: {new_path}")
    print("\nВыгода: теперь для работы с файлом 'info.txt' достаточно просто указать его имя!")

    print("-" * 80)
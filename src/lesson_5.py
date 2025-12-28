import os
import datetime

source = 'draft_report.txt'
destination = 'final_report.txt'

source_2 = 'new_document.txt'
destination_2 = 'archive/new_document.txt'  # Указываем путь внутрь папки

source_3 = 'project/drafts/document.txt'
destination_3 = 'archive/2025/final_document.txt'
destination_3_folder = "archive/2025"

# Имя файла, который будет жить всего несколько секунд
disposable_file = 'file_to_destroy.tmp'

file_to_delete = 'maybe_exists.log'

config_file = 'settings.ini'

# Имя файла для нашего эксперимента с os.stat()
filename = 'file_info.txt'

if __name__ == "__main__":
    # ========== Переименование файла =============
    # Сначала создадим файл для эксперимента
    with open('draft_report.txt', 'w') as f:
        f.write('This is a draft.')
    print("Файл 'draft_report.txt' создан.")

    # Теперь переименуем его
    print(f"Переименовываю '{source}' в '{destination}'...")
    os.rename(source, destination)
    print("Файл успешно переименован!")
    os.remove(destination)
    print("*" * 80)

    # ========== Перемещение файла в другую папку =============
    # Подготовим среду: папка и файл в ней
    os.makedirs('archive', exist_ok=True)
    with open('new_document.txt', 'w') as f:
        f.write('Some data.')

    print("Файл 'new_document.txt' создан в корне проекта.")

    # Теперь переместим файл в папку 'archive'
    print(f"Перемещаю '{source_2}' в папку 'archive'...")
    os.rename(source_2, destination_2)
    os.remove(destination_2)
    print("Файл успешно перемещен!")
    print("*" * 80)

    # ========== Перемещение файла в новую сложную структуру папок =============
    # 1. Создадим сложную структуру для исходного файла
    os.makedirs('project/drafts', exist_ok=True)
    with open('project/drafts/document.txt', 'w') as f:
        f.write('data')

    print("Создана структура 'project/drafts/document.txt'.")

    # 2. Теперь используем os.renames для перемещения в совершенно новое место

    print(f"\nПеремещаю '{source_3}' в '{destination_3}' с помощью os.renames...")
    os.renames(source_3, destination_3)

    print("\nОперация завершена. Проверьте структуру папок!")
    os.remove(destination_3)
    os.rmdir(destination_3_folder)
    os.rmdir(destination_3_folder.split("/")[0])  # Удаляем папку 'archive', если она пуста
    print("*" * 80)

    # ========== Создание и удаление временного файла =============
    # Этап 1: Создание "жертвы"
    print(f"Создаю временный файл: '{disposable_file}'")
    with open(disposable_file, 'w') as f:
        f.write('Я существую только для того, чтобы быть удаленным.')

    # Проверяем, что он действительно появился в папке
    print("Файл успешно создан.")

    # Этап 2: Удаление
    print(f"\nПриступаю к удалению файла '{disposable_file}'...")
    os.remove(disposable_file)
    print("Операция завершена. Файл стерт навсегда.")
    print("*" * 80)

    # ========== Проверка существования файла перед удалением =============
     # Спрашиваем: "Этот файл существует?"
    if os.path.exists(file_to_delete):
        # Если ответ "Да", то удаляем
        print(f"Файл '{file_to_delete}' найден. Удаляю.")
        os.remove(file_to_delete)
    else:
        # Если ответ "Нет", то просто сообщаем об этом
        print(f"Файл '{file_to_delete}' не найден. Удалять нечего.")
        print("*" * 80)

    # ========== Удаление файла с обработкой исключений =============
    print(f"\nПытаюсь удалить файл '{file_to_delete}' с обработкой исключений...")
     # Пытаемся удалить файл, даже если его может не быть
    try:
        # Смело пытаемся удалить
        os.remove(file_to_delete)
        print(f"Файл '{file_to_delete}' был найден и успешно удален.")
    except FileNotFoundError:
        # Если произошла ошибка "Файл не найден", выполняем этот блок
        print(f"Файл '{file_to_delete}' и так не существовал. Все в порядке.")
    print("*" * 80)

    # ========== Проверка существования пути (файла или папки) =============
    # 1. Подготовим среду для эксперимента
    # Создадим файл, чтобы он точно существовал
    with open('data_file.txt', 'w') as f:
        f.write('some data')
    # Создадим папку, чтобы она тоже точно существовала
    os.makedirs('data_folder', exist_ok=True)

    # 2. Теперь начнем проверки
    path_to_file = 'data_file.txt'
    path_to_folder = 'data_folder'
    non_existent_path = 'ghost_file.txt'

    print(f"--- Начинаю проверку ---")

    # Проверка №1: Существующий файл
    if os.path.exists(path_to_file):
        print(f"✅ Путь '{path_to_file}' СУЩЕСТВУЕТ.")
    else:
        print(f"❌ Путь '{path_to_file}' НЕ существует.")

    # Проверка №2: Существующая папка
    if os.path.exists(path_to_folder):
        print(f"✅ Путь '{path_to_folder}' СУЩЕСТВУЕТ.")
    else:
        print(f"❌ Путь '{path_to_folder}' НЕ существует.")

    # Проверка №3: Несуществующий путь
    if os.path.exists(non_existent_path):
        print(f"✅ Путь '{non_existent_path}' СУЩЕСТВУЕТ.")
    else:
        print(f"❌ Путь '{non_existent_path}' НЕ существует.")

    # 3. Не забудем убрать за собой (хорошая практика)
    os.remove(path_to_file)
    os.rmdir(path_to_folder)
    print("*" * 80)

    # ========== Создание файла настроек, если его нет =============
    if not os.path.exists(config_file):
        print(f"Файл '{config_file}' не найден. Создаю стандартный файл настроек.")
        with open(config_file, 'w') as f:
            f.write('[Settings]\nuser=default\n')
    else:
        print(f"Файл '{config_file}' уже существует. Использую его.")
    print("*" * 80)

    # ========== Получение информации о файле с os.stat() =============

    # Создаем файл
    with open(filename, 'w') as f:
        f.write('Это первая строка.\nЭто вторая строка.\n')

    print(f"--- Получаю информацию о файле '{filename}' ---")

    # 1. Вызываем os.stat() и получаем объект с метаданными
    stat_info = os.stat(filename)

    # 2. Выводим самую полезную информацию
    print(f"Размер файла: {stat_info.st_size} байт")

    # 3. Время хранится в формате "секунд с начала эпохи", что неудобно.
    # Преобразуем его в читаемый формат с помощью модуля datetime.
    modification_time = datetime.datetime.fromtimestamp(stat_info.st_mtime)
    creation_time = datetime.datetime.fromtimestamp(stat_info.st_ctime)

    print(f"Время последнего изменения: {modification_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Время создания (на Windows): {creation_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Не забудем убрать за собой
    os.remove(filename)
    print("*" * 80)
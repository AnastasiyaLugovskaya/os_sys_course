import os
import sys
from typing import Optional

from sorter_values import SorterValues


class Sorter:
    def __init__(self):
        self.command_name = __file__
        self.dir_name = self.check_args()



    def check_args(self):
        """
        Проверяет аргументы командной строки.
        1. Проверяет, что передан ровно один аргумент (имя папки).
        2. Проверяет, что указанная директория существует и является директорией.
        3. Выводит сообщения об ошибках в stderr и завершает программу с соответствующим кодом выхода.
        4. Если все проверки пройдены, возвращает имя директории для дальнейшей обработки.
        :return:
        """
        try:
            # 1. Проверяем, что нам передали ровно один аргумент (имя папки для сортировки)
            self.check_args_len()
            dir_name = sys.argv[1]

            # 2. Проверяем, существует ли директория и является ли она директорией
            self.check_dir_exists(dir_name)
            self.check_is_dir(dir_name)

            # 3. Если все проверки пройдены, возвращаем имя директории
            base_path = os.getcwd()
            return os.path.join(base_path, dir_name)
        finally:
            print("-" * 80)

    def check_is_dir(self, dir_name: str):
        """
        Проверяет, что указанный путь является директорией.
        Если путь не является директорией, выводит сообщение об ошибке в stderr и завершает программу с кодом 3.
        :param dir_name: Имя директории для проверки.
        :return: None
        """
        if not os.path.isdir(dir_name):
            sys.stderr.write(f"Ошибка: Путь '{dir_name}' не является директорией.\n")
            sys.exit(3)  # Код 3 - не директория

    def check_dir_exists(self, dir_name: str):
        """
        Проверяет, что указанная директория существует.
        Если директория не существует, выводит сообщение об ошибке в stderr и завершает программу с кодом 2.
        :param dir_name: Имя директории для проверки.
        :return: None
        """
        if not os.path.exists(dir_name):
            sys.stderr.write(f"Ошибка: Директория '{dir_name}' не найдена.\n")
            sys.exit(2)  # Код 2 - директория не найдена

    def check_args_len(self):
        """
        Проверяет, что передан ровно один аргумент (имя папки).
        Если количество аргументов неверно, выводит сообщение об ошибке в stderr и завершает программу с кодом 1.
        :return: None
        """
        if len(sys.argv) != 2:
            # Выводим сообщение об ошибке в stderr (правильное место для ошибок!)
            sys.stderr.write(
                f"Ошибка: Укажите ровно один аргумент - имя папки."
                f"\nПример использования: python {os.path.basename(self.command_name)} <имя>\n"
            )
            sys.exit(1)  # Код 1 - ошибка использования

    def sort(self):
        """
        Основной метод для сортировки файлов в указанной директории.
        :return:
        """
        base_path = os.getcwd()
        # 1. Получаем список файлов в директории
        files = self.get_file_list()
        print(f"\nВ целевой папке найдены следующие файлы для сортировки: \n{files}")
        categories_dict = {}
        for file in files:
            ext = self.get_file_extention(file)
            target_folder = SorterValues.SORTING_CATEGORIES.get(ext)
            if target_folder:
                if target_folder not in categories_dict:
                    categories_dict[target_folder] = []
                categories_dict[target_folder].append(file)
            else:
                sys.stderr.write(f"\nОшибка: Неизвестное расширение файла '{file}'. Файл пропущен.\n")
        print(f"\nОтобранные файлы будут распределены по следующим категориям: \n{categories_dict}")
        # 2. Создаем целевые папки и перемещаем файлы
        for category, files in categories_dict.items():
            target_dir = self.create_sub_dir(category)
            for file in files:
                self.move_file(category, file, target_dir)


    def get_file_list(self) -> list:
        """
        Получает список файлов в указанной директории.
        :return: list: Список имен файлов в директории.
        """
        return [
        file for file in os.listdir(self.dir_name)
        if os.path.isfile(os.path.join(self.dir_name, file))
    ]

    def get_file_extention(self, file: str) -> str:
        """
        Получает расширение файла в нижнем регистре.
        Если расширения нет, возвращает пустую строку.
        :param file: Имя файла.
        :return: str: Расширение файла в нижнем регистре или пустая строка.
        """
        if '.' not in file:
            return ''

        return file.rsplit('.', 1)[-1].lower()


    def create_sub_dir(self, category: str) -> str:
        """
        Создает целевую поддиректорию для указанной категории, если она не существует.
        :param category: Категория файла в зависимости от его расширения.
        :return: str: Путь к созданной или существующей целевой директории.
        """
        target_dir = os.path.join(self.dir_name, category)
        os.makedirs(target_dir, exist_ok=True)
        return target_dir


    def move_file(self, category: str, file: str, target_dir: str):
        """
        Перемещает файл в указанную целевую директорию.
        :param category: Категория файла в зависимости от его расширения.
        :param file: Имя файла для перемещения.
        :param target_dir: Целевая директория для перемещения файла.
        :return:
        """
        source_path = os.path.join(self.dir_name, file)
        destination_path = os.path.join(target_dir, file)
        os.rename(source_path, destination_path)
        print(f"Перемещен файл '{file}' в папку '{category}'.")

if __name__ == '__main__':
    sorter = Sorter()
    sorter.sort()


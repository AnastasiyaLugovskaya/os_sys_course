import os, sys

class LogAnalyzer:
    def __init__(self):
        self.command_name = __file__
        self.log_file = self.check_args()
        self.word = self.get_keyword()

    def check_args(self):
        """
        Проверяет аргументы командной строки.
        1. Проверяет, что передан ровно два аргумента (имя файла с логами и ключевое слово для поиска).
        2. Проверяет, что указанная директория существует и является файлом.
        3. Выводит сообщения об ошибках в stderr и завершает программу с соответствующим кодом выхода.
        4. Если все проверки пройдены, возвращает имя файла для дальнейшей обработки.
        :return: str
        """
        try:
            # 1. Проверяем, что нам передали ровно два аргумента (имя файла с логами и ключевое слово для поиска)
            self.check_args_len()
            file_name = sys.argv[1]

            # 2. Проверяем, существует ли указанный путь к файлу и является ли он файлом
            self.check_dir_exists(file_name)
            self.check_is_file(file_name)

            # 3. Если все проверки пройдены, возвращаем имя файла
            base_path = os.getcwd()
            return os.path.join(base_path, file_name)
        finally:
            print("-" * 80)


    def check_args_len(self):
        """
        Проверяет, что передано ровно два аргумента (имя файла с логами и ключевое слово для поиска).
        Если количество аргументов неверно, выводит сообщение об ошибке в stderr и завершает программу с кодом 1.
        :return: None
        """
        if len(sys.argv) != 3:
            # Выводим сообщение об ошибке в stderr (правильное место для ошибок!)
            sys.stderr.write(
                f"Ошибка: Укажите ровно два аргумента - имя файла с логами и ключевое слово для поиска."
                f"\nПример использования: python {os.path.basename(self.command_name)} "
                f"<имя файла с логами> <ключевое слово для поиска>\n"
            )
            sys.exit(1)  # Код 1 - ошибка использования


    def check_is_file(self, file_name: str):
        """
        Проверяет, что указанный путь является файлом.
        Если путь не является файлом, выводит сообщение об ошибке в stderr и завершает программу с кодом 3.
        :param file_name: Имя файла для проверки.
        :return: None
        """
        if not os.path.isfile(file_name):
            sys.stderr.write(f"Ошибка: Путь '{file_name}' не является файлом.\n")
            sys.exit(3)  # Код 3 - не файл


    def check_dir_exists(self, file_name: str):
        """
        Проверяет, что указанная директория существует.
        Если директория не существует, выводит сообщение об ошибке в stderr и завершает программу с кодом 2.
        :param file_name: Имя директории для проверки.
        :return: None
        """
        if not os.path.exists(file_name):
            sys.stderr.write(f"Ошибка: Директория '{file_name}' не найдена.\n")
            sys.exit(2)  # Код 2 - директория не найдена

    def get_keyword(self):
        """
        Возвращает ключевое слово, полученное из аргументов командной строки
        :return: str
        """
        keyword = sys.argv[2].lower()
        return keyword

    def read_log_file(self):
        """
        Читает построчно файл с логами и выводит на экран строки, содержащие ключевое слово
        :return: None
        """
        try:
            with open(self.log_file, "r", encoding="utf-8") as file:
                for i, line in enumerate(file, start=1):
                    line = line.strip()
                    if self.word in line.lower():
                        print(f"{i}.{line}")
        except FileNotFoundError as e:
            sys.stderr.write(f"Ошибка: Не удалось найти файл для чтения. {e}\n")
            sys.exit(2) # Код 2 - директория не найдена
        except UnicodeDecodeError as e:
            sys.stderr.write(f"Ошибка: Не удалось прочитать файл. {e}\n")
            sys.exit(4) # Код 4 - ошибка декодирования
        except Exception as e:
            sys.stderr.write(f"Ошибка: {e}\n")
            sys.exit(5) # Код 5 - непредвиденные исключения
        sys.exit(0) # Код 0 - штатное завершение работы

if __name__ == '__main__':
    analyzer = LogAnalyzer()
    analyzer.read_log_file()


import os

system_name = os.name
current_directory = os.getcwd()
report_path = current_directory + "\\report.txt"

if os.name == 'nt': # Для Windows
    username_variable = 'USERNAME'
    home_variable = 'USERPROFILE'
else: # Для macOS и Linux
    username_variable = 'USER'
    home_variable = 'HOME'

username = os.environ[username_variable]
home_directory = os.environ[home_variable]
system_path = os.environ['PATH']


if __name__ == "__main__":
    print(f"Имя моей операционной системы: {system_name}")
    print(f"Я запущен из папки: {current_directory}")
    print(f"Я собираюсь создать отчет здесь: {report_path}")
    print("-" * 80)
    print(f"Имя пользователя в системе: {username}")
    print(f"Путь к домашней директории: {home_directory}")
    print(f"\nПеременная PATH: {system_path}")





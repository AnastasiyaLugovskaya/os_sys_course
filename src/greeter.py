import sys
import os

# sys.argv[0] - это всегда имя самого файла скрипта
# sys.argv[1] - это первый аргумент, который мы передали

command_name = __file__
wrong_arg_count_message = (
    f"\nОшибка: Неверное количество аргументов. \nПример использования: python {os.path.basename(command_name)} <имя>"
)

try:
    name = sys.argv[1]
    if len(sys.argv) == 2:
        print(f"\nПривет, {name}!")
    else:
        print(wrong_arg_count_message)
except IndexError:
    print(wrong_arg_count_message)
print("=" * 80)
import os
import sys


if __name__ == "__main__":
    print("--- Проверяем модуль os ---")
    print(f"Мой скрипт находится в папке: {os.getcwd()}")

    print("\n--- Проверяем модуль sys ---")
    print(f"Я использую версию Python: {sys.version}")
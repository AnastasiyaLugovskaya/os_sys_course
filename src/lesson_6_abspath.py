import os

# --- Определим несколько относительных путей для теста ---
path1 = 'my_file.txt'          # Файл в текущей папке
path2 = '.'                    # Указатель на текущую папку
path3 = '..'                   # Указатель на родительскую папку
path4 = os.path.join('data', 'report.csv') # Вложенный путь

# --- Превратим их все в абсолютные ---
abs_path1 = os.path.abspath(path1)
abs_path2 = os.path.abspath(path2)
abs_path3 = os.path.abspath(path3)
abs_path4 = os.path.abspath(path4)

if __name__ == '__main__':
    print(f"Моя текущая рабочая директория: {os.getcwd()}\n")
    print(f"Относительный: '{path1}' -> Абсолютный: {abs_path1}")
    print(f"Относительный: '{path2}'   -> Абсолютный: {abs_path2}")
    print(f"Относительный: '{path3}'  -> Абсолютный: {abs_path3}")
    print(f"Относительный: '{path4}' -> Абсолютный: {abs_path4}")
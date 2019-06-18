import os
import shutil as su

def create_dir(dir_path):
    try:
        os.mkdir(os.path.join(os.getcwd(), dir_path))
        print(f'Директория {dir_path} создана в текущей')
    except FileExistsError:
        print(f'Директория {dir_path} уже существует')
    except:
        print(f'Ошибка создания директории {dir_path}')

def delete_dir(dir_path):
    try:
        os.rmdir(os.path.join(os.getcwd(), dir_path))
        print(f'Директория {dir_path} удалена из текущей')
    except FileNotFoundError:
        print(f'Директории {dir_path} не существует')
    except:
        print(f'Ошибка удаления директории {dir_path}')

def list_cur_files(dr):
    for f in os.listdir(dr):
        print(f)

def copy_file(name):
    try:
        name2 = name +'2'
        su.copy(name, name2)
        print('Копия файла создана как ', name2)
    except OSError:
        print('Ошибка копирования файла')

def rem_file(name):
    try:
        os.remove(name)
        print('Файл успешно удален')
    except OSError:
        print('Ошибка удаления файла')

def chg_dir(name):
    try:
        os.chdir(name)
    except OSError:
        print('Ошибка смены каталога')

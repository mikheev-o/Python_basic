# Запускать с параметрами:
# python hw05_hard_args.py key [name]
import os
import sys
import os_lib1 as ol
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаление указанног файла")
    print("cd <full_path or relative_path> - смена текущей директории на указанную")
    print("ls - вывод полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not fd_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), fd_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(fd_name))
    except FileExistsError:
        print('директория {} уже существует'.format(fd_name))

def copy_file():
    if not fd_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    ol.copy_file(fd_name)

def rem_file():
    if not fd_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if input(f"Вы уверены, что хотите удалить файл {fd_name}? (ДА = 'Y')") == "Y":
        ol.rem_file(fd_name)

def chg_dir():
    print(os.getcwd())
    if not fd_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    ol.chg_dir(fd_name)
    print(os.getcwd())

def full_path():
    print('Текущий полный путь '+ os.getcwd())

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": rem_file,
    "cd": chg_dir,
    "ls": full_path,
    "ping": ping
}

try:
    fd_name = sys.argv[2]
except IndexError:
    fd_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

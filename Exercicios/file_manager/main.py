import os
import shutil

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CWD_PATH = os.path.join(os.getcwd(), 'Exercicios', 'file_manager')
BACKUP_PATH = os.path.join(os.getcwd(), 'Exercicios', 'file_manager', 'backup')


def show_direct(path):
    for root, _, files in path:
        print(f"{os.path.basename(root)}/")

        for file in files:
            print(f"  {file}")

def file_sizes(path):
    for root, _, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)

            sizeinbytes = os.path.getsize(path)
            sizeinmegas = sizeinbytes / (1024 * 1024)
            print(f'Name file: {file}\n Size: {sizeinmegas:.2f}MB\n')

def rename_files():
    oldname = input('Actual file name: ')
    newname = input('New file name: \n')

    for root, dirs, files in os.walk(ROOT_PATH):
        if 'backup' in dirs:
            dirs.remove('backup')
        for file in files:
            if file == oldname:
                oldpath = os.path.join(root, file)
                newpath = os.path.join(root, newname)
                os.rename(oldpath, newpath)
                print('\nSucessfully renamed!\n')
                return
    print('\nFile not found!\n')

def move_file():
    filename = input('Name file: ')
    newpath = input('New file folder: ')
    for root, dirs, files in os.walk(ROOT_PATH):
        if 'backup' in dirs:
            dirs.remove('backup')
        for file in files:
            if file == filename:
                oldpath = os.path.join(root, file)
                newpath = os.path.join(ROOT_PATH, newpath)
                shutil.move(oldpath, newpath)
                return
    print('\nFile not found!\n')

while True:
    print('\n==== FILE MANAGER ====')
    print('\n1 - Show directory tree')
    print('2 - Show file sizes')
    print('3 - Create backup')
    print('4 - Rename file')
    print('5 - Move file')
    print('6 - Delete backup')
    print('0 - Exit')
    choice = input('Choice a option: ')

    if choice == '1':
        show_direct(os.walk(ROOT_PATH))
    elif choice == '2': 
        file_sizes(CWD_PATH)
    elif choice == '3':
        try:
            shutil.copytree(ROOT_PATH, BACKUP_PATH)
        except FileExistsError:
            print('\nBackup already exists!')
    elif choice == '4':
        rename_files()
    elif choice == '5':
        move_file()
    elif choice == '6':
        try:
            shutil.rmtree(BACKUP_PATH)
        except FileNotFoundError:
           print('Backup not found!')
    elif choice == '0':
        print('Closing program...')
        break
    else:
        print('Invalid option!')


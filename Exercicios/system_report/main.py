import calendar
from datetime import datetime
import locale
import os


def list_files(path):
    try:
        return [dir for dir in os.listdir(path)]
    except FileNotFoundError:
        return 'Error: The directory was not found!'
    except PermissionError:
        return 'Error: Permission denied to access this folder.'

def list_folders(path):
    return [f for f in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, f))]

def check_path(path):
    file_path = os.path.join(current_path, path)
    if os.path.exists(file_path):
        print('Yes\n')
    else:
        print('No\n')

def show_calendar():
    today = datetime.now()
    month = int(input('Choose a month (1-12): '))
    print(calendar.month(today.year, month))

print('==== SYSTEM REPORT ====\n')
print('Current directory:')
current_path = os.path.dirname(os.path.abspath(__file__))
print(f'{current_path}, \n')

print('Files in current directory:\n')
files_ = list_files(current_path)
for f in files_:
    print(f)
print()

print('Folders:\n')
folders = list_folders(current_path)
for f in folders:
    print(f)
print()

print('Does README.md exist?')
check_path('README.md')

print('Does config.json exist?')
check_path('config.json')

print('Is images a directory?')
check_path('images')

print('Is notes.txt a file')
check_path('notes.txt')

print('Today:\n')
today = datetime.now()
today = today.strftime('%A\n%d %B %Y')
print(f'{today}\n')
locale.setlocale(locale.LC_ALL, '')

today = datetime.now()
print(calendar.month(today.year, today.month))

show_calendar()


import os

def clean_console():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
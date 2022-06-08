from data.file_data import get_default_file
from helpers.clean_console import clean_console


def file_menu():
    menu_options = {
    1: 'Load default file',
    2: 'Load another txt file',
    3: 'Return main menu',
    }

    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
        
    while(True):
        option_menu = ''
        try:
            option_menu = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option_menu == 1:
            data =  get_default_file()
            clean_console()
            return data
        elif option_menu == 2:
            print('cargar otro archivo')
        elif option_menu == 3:
            option_menu = ''
            clean_console()
            break
        else:
            print('Invalid option. Please enter a number between 1 and 3.')


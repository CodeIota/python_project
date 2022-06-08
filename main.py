from helpers.clean_console import clean_console
from modules.file_menu import file_menu
from modules.services_menu import services_menu
from data.transform_data import get_person_data 

file = None

menu_options = {
    1: 'File',
    2: 'Acctions',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            clean_console()
            file = file_menu()
        elif option == 2:
            # try:
                clean_console()
                services_menu(get_person_data(file))
            # except:
                print('\nPlease to use the services you need a file with data')
        elif option == 3:
            print('Thanks for use my project :)')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
from doctest import master
from Person import Person
import os


def get_person_data() -> dict:
    data = {}
    file = open('competencia.txt').readlines()

    for person_key, line in enumerate(file):
        row_data = line.split(',')
        dni, first_lastname, second_lastname, name, initial_second_name, gender, age, hours, minutes, seconds = [i.strip() for i in row_data]
        person = Person(dni, first_lastname, second_lastname, name, initial_second_name, gender, age, hours, minutes, seconds)
        data[person_key] = person
    
    return data

def define_group() -> dict:
    job_group = {'junior': {}, 'senior': {}, 'master': {}}
    persons_dict: dict = get_person_data()
    for key, person in persons_dict.items(): 
        if int(person.age) > 40:
            job_group['master'][key] = person
        if 25 <= int(person.age) <= 40:
            job_group['senior'][key] = person
        if int(person.age) <=25:
            job_group['junior'][key] = person
    return job_group

### helpers/to_table

from prettytable import PrettyTable

def to_table(headers, data):
    table = PrettyTable()
    table.field_names(headers)
    table.add_rows(data.items())
    # for person in data.item():
    #     table.add_row

### no1 services/participants_list
def participants_list() -> list:    
    return get_person_data()        

### no 2 services get_total_participants
def get_total_participants(data: dict) -> int:
    return len(data)


### no3 services/get_total participants

def get_total_participants_by_group(data: dict):
    juniors = len(data['junior'])
    seniors = len((data['senior']))
    masters = len(data['master'])
    data = [juniors, seniors, masters]
    return data

### no4 services/get_total_participants_by_gender

def get_total_participants_by_gender() -> list:
    male, female = (0, 0)
    return [male, female]

### n5 services/get_winners_by_group
def get_winners_by_group() -> list:
    junior, senior, master = (0, 0, 0)
    return [junior, senior, master]

### n6 services/get_winners_by_gender
def get_winners_by_gender() -> list:
    male, female = (0, 0)
    return [male, female]

### n7 services/get_winners_by_gender_and_groups
def get_winners_by_gender_and_groups() -> tuple:
    pass

### n8 services/get_general_winner
def get_general_winner():
    pass

### n9 services/get_histogram_by_group  
def get_histogram_by_group():
    pass

### n10 services/average_time_by_group_and_gender
def average_time_by_group_and_gender():
    pass

## helpers/clean_console 
def clean_console():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

## modules/file_menu/file_menu

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
            print('cargar archivo predeterminado')
        elif option_menu == 2:
            print('cargar otro archivo')
        elif option_menu == 3:
            option_menu = ''
            clean_console()
            break
        else:
            print('Invalid option. Please enter a number between 1 and 3.')


## modules/main_menu/services_menu

def services_menu():
    menu_options = {
        1: 'Total participants list',
        2: 'Total number of participants',
        3: 'Total number of participants by group',
        4: 'Total number of participants by gender',
        5: 'Winners by group',
        6: 'Winners by gender',
        7: 'Winners by group and gender',
        8: 'General winner',
        9: 'Histrogram of participants by group',
        10: 'Average number of participants by group and gender', 
        11: 'Retrun main menu'
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
            headers = ['dni', 'first_lastname', 'second_lastname', 'name', 'initial_second_name', 'gender', 'age', 'hours', 'minutes', 'seconds']
            data = get_total_participants()
            to_table(headers, data)
        elif option_menu == 2:
            print('option 2 selected')
        elif option_menu == 3:
            clean_console()
            print('option 3 selected')
        elif option_menu == 4:
            print('option 4 selected')
        elif option_menu == 5:
            clean_console()
            print('option 5 selected')
        elif option_menu == 6:
            print('option 6 selected')
        elif option_menu == 7:
            clean_console()
            print('option 7 selected')
        elif option_menu == 8:
            print('option 8 selected')
        elif option_menu == 9:
            clean_console()
            print('option 9 selected')
        elif option_menu == 10:
            clean_console()
            print('option 10 selected')
        elif option_menu == 11:
            clean_console()
            print('option 11 selected')
        else:
            print('Invalid option. Please enter a number between 1 and 11.')

## modules/main_menu/services_menu

menu_options = {
    1: 'File',
    2: 'Acctions',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

import os


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
            file_menu()
        elif option == 2:
            clean_console()
            services_menu()
        elif option == 3:
            print('Thanks for use my project :)')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
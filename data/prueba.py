from dataclasses import dataclass
import datetime
import functools
from Person import Person
import os

def get_default_file ():
    return open('competencia.txt').readlines()

def open_another_file (name: str):
    try: 
        pass
    except:
        pass


def get_person_data() -> dict:
    data = {}
    file = get_default_file()
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

def full_name(person):
    return person.name + ' ' + person.initial_second_name + '. ' + person.first_lastname + ' ' + person.second_lastname

def to_table(headers, data):
    table = PrettyTable(headers)
    for person in data.item():
        table.add_row(person.dni, full_name(person), person.gender, person.age)

### no1 services/participants_list
def participants_list() -> list:    
    return get_person_data()        

### no 2 services get_total_participants
def get_total_participants(data: dict) -> int:
    return len(data)


### no3 services/get_total participants

def get_total_participants_by_group(data: dict)-> tuple:
    juniors = len(data['junior'])
    seniors = len((data['senior']))
    masters = len(data['master'])
    data = (juniors, seniors, masters)
    return data

### no4 services/get_total_participants_by_gender

def get_total_participants_by_gender(data: dict) -> tuple:
    total_male, total_female = (0, 0)
    for participant in data.values():
        if participant.gender == 'M':
            total_male += 1
        if participant.gender == 'F':
            total_female += 1
    return (total_male, total_female)

def to_seconds(person: Person)-> int:
    return int(person.seconds) + int(person.minutes)*60 + int(person.hours)* 3600


def check_time(participant1: Person, participant2: Person)-> Person:
    time_participant1 = to_seconds(participant1)
    time_participant2 = to_seconds(participant2)

    if time_participant2 < time_participant1:
        return participant2
    else: return participant1



### n5 services/get_winners_by_group
def get_winners_by_group() -> list:
    data = define_group()
    junior = data['junior'].values()
    senior = data['senior'].values()
    master = data['master'].values()

    winner_junior = functools.reduce(check_time, junior) 
    winner_senior = functools.reduce(check_time, senior)
    winner_master = functools.reduce(check_time, master)

    return [['junior', full_name(winner_junior), str(datetime.timedelta(seconds=to_seconds(winner_junior)))], 
    ['senior', full_name(winner_senior), str(datetime.timedelta(seconds=to_seconds(winner_senior)))], 
    ['master', full_name(winner_master), str(datetime.timedelta(seconds=to_seconds(winner_master)))]]

### n6 services/get_winners_by_gender

def separate_gender(data: dict):
    male, female = [], []
    
    for person in data.values():
        if person.gender == 'M':
            male.append(person)
        if person.gender == 'F':
            female.append(person)

    return (male, female)

def get_winners_by_gender() -> list:
    data = get_person_data()
    male_list, female_list = separate_gender(data)
    winner_male = functools.reduce(check_time, male_list)
    winner_female = functools.reduce(check_time, female_list)

    return [['male', full_name(winner_male), str(datetime.timedelta(seconds=to_seconds(winner_male)))],
    ['female', full_name(winner_female), str(datetime.timedelta(seconds=to_seconds(winner_female)))]
    ]

### n7 services/get_winners_by_gender_and_groups
def get_winners_by_gender_and_groups() -> tuple:
    data = define_group()
    junior = data['junior']
    senior = data['senior']
    master = data['master']

    list_male_junior, list_female_junior = separate_gender(junior)
    list_male_senior, list_female_senior = separate_gender(senior)
    list_male_master, list_female_master = separate_gender(master)

    winner_male_junior = functools.reduce(check_time, list_male_junior)
    winner_female_junior = functools.reduce(check_time, list_female_junior)
    winner_male_senior = functools.reduce(check_time, list_male_senior)
    winner_female_senior = functools.reduce(check_time, list_female_senior)
    winner_male_master = functools.reduce(check_time, list_male_master)
    winner_female_master = functools.reduce(check_time, list_female_master)

    return [['junior', full_name(winner_male_junior), full_name(winner_female_junior)],
    ['senior', full_name(winner_male_senior), full_name(winner_female_senior)],
    ['master', full_name(winner_male_master), full_name(winner_female_master)]]


### n8 services/get_general_winner
def get_general_winner():
    data = get_person_data().values()
    winner = functools.reduce(check_time, data)
    return full_name(winner)

### n9 services/get_histogram_by_group  
def get_histogram_by_group():
    pass

### n10 services/average_time_by_group_and_gender

def gender_by_group(data: dict, group: str)-> tuple:
    group = data[group]
    total_male_group, total_female_group = get_total_participants_by_gender(group)

    return (total_male_group, total_female_group)


def average_time_by_group_and_gender():
    data = define_group()
    juniors = len(data['junior'])
    seniors = len((data['senior']))
    masters = len(data['master'])

    male_junior, female_junior = gender_by_group(data, 'junior')
    male_senior, female_senior = gender_by_group(data, 'senior')
    male_master, female_master = gender_by_group(data, 'master')

    return [ ['juniors', str(round(male_junior/juniors, 3) * 100 ) + '%', str(round(female_junior/juniors, 3)* 100) + '%'],
        ['seniors', str(round(male_senior/seniors, 3) * 100) + '%', str(round(female_senior/seniors, 3)* 100) + '%'],
        ['masters', str(round(male_master/masters, 3) * 100) + '%', str(round(female_master/masters, 3)* 100) + '%']
    ]
    



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
            headers = ['dni', 'full name', 'gender', 'age']
            participants = participants_list()
            table = PrettyTable(headers)
            for participant in participants.values():
                table.add_row([participant.dni, participant.name + ' ' + participant.initial_second_name + ' ' + participant.first_lastname + ' ' + participant.second_lastname, participant.gender, participant.age])
            print(table)
        elif option_menu == 2:
            data = get_person_data()
            print('total participants: ', len(data))
        elif option_menu == 3:
            data = define_group()
            headers = ['juniors', 'seniors', 'masters']
            juniors, seniors, masters = get_total_participants_by_group(data)
            table = PrettyTable(headers)
            table.add_row([juniors, seniors, masters])
            print(table)
        elif option_menu == 4:
            data = participants_list()
            male, female = get_total_participants_by_gender(data)
            table = PrettyTable(['Male', 'Female'])
            table.add_row([male, female])
            print(table)
        elif option_menu == 5:
            data = get_winners_by_group()
            table = PrettyTable(['Group', 'Winners', 'Time'])
            table.add_rows(data)
            print(table)
        elif option_menu == 6:
            data = get_winners_by_gender()
            table = PrettyTable(['Gender', 'Winner', 'Time'])
            table.add_rows(data)
            print(table)
        elif option_menu == 7:
            data = get_winners_by_gender_and_groups()
            table = PrettyTable(['Group', 'Male', 'Female'])
            table.add_rows(data)
            print(table)
        elif option_menu == 8:
            winner = get_general_winner()
            print(winner)
        elif option_menu == 9:
            clean_console()
            print('option 9 selected')
        elif option_menu == 10:
            data = average_time_by_group_and_gender()
            table = PrettyTable([' ', 'Male', 'Female'])
            table.add_rows(data)
            # table.add_column(['junior', 'senior', 'master'])
            print(table)
        elif option_menu == 11:
            clean_console()
            break
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
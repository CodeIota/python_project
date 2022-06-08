from prettytable import PrettyTable

from helpers.clean_console import clean_console
from data.transform_data import define_group
from helpers.full_name import full_name
from services.get_histogram_per_group import get_histogram_per_group
from services.get_total_participants import get_total_participants
from services.participants_list import participants_list
from services.get_total_participants_per_group import get_total_participants_by_group
from services.get_total_participants_per_gender import get_total_participants_by_gender
from services.get_winners_per_group import get_winners_by_group
from services.get_winners_per_gender import get_winners_by_gender
from services.get_winners_per_gender_and_groups import get_winners_by_gender_and_groups
from services.get_general_winner import get_general_winner
from services.average_time_by_group_and_gender import average_time_by_group_and_gender


def services_menu(participants):
    
    participants_data = participants
    groups = define_group(participants)

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
            data = participants_data
            result = participants_list(data)
            table = PrettyTable(['dni', 'full name', 'gender', 'age'])
            for participant in result.values():
                table.add_row([participant.dni, full_name(participant), participant.gender, participant.age])
            print(table)
        elif option_menu == 2:
            print('total participants: ', get_total_participants(participants_data))
        elif option_menu == 3:
            data = groups
            juniors, seniors, masters = get_total_participants_by_group(data)
            table = PrettyTable(['juniors', 'seniors', 'masters'])
            table.add_row([juniors, seniors, masters])
            print(table)
        elif option_menu == 4:
            data = participants_data
            male, female = get_total_participants_by_gender(data.values())
            table = PrettyTable(['Male', 'Female'])
            table.add_row([male, female])
            print(table)
        elif option_menu == 5:
            data = get_winners_by_group(groups)
            table = PrettyTable(['Group', 'Winners', 'Time'])
            table.add_rows(data)
            print(table)
        elif option_menu == 6:
            data = get_winners_by_gender(participants_data)
            table = PrettyTable(['Gender', 'Winner', 'Time'])
            table.add_rows(data)
            print(table)
        elif option_menu == 7:
            data = get_winners_by_gender_and_groups(groups)
            table = PrettyTable(['Group', 'Male', 'Female'])
            table.add_rows(data)
            print(table)
        elif option_menu == 8:
            winner = get_general_winner(participants)
            print(winner)
        elif option_menu == 9:
            get_histogram_per_group(groups)
        elif option_menu == 10:
            data = average_time_by_group_and_gender(groups)
            table = PrettyTable([' ', 'Male Time', 'Female Time'])
            table.add_rows(data)
            print(table)
        elif option_menu == 11:
            clean_console()
            break
        else:
            print('Invalid option. Please enter a number between 1 and 11.')
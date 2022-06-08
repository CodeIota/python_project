import datetime
import functools
from helpers.time_helper import to_seconds
from services.get_total_participants_per_gender import get_total_participants_by_gender
from services.get_total_participants_per_group import get_total_participants_by_group


def sum_time(participants):
    male_time, female_time = (0,0)
    total_male_group, total_female_group = get_total_participants_by_gender(participants)
    for participant in participants:
        if participant.gender == 'M':
            male_time += to_seconds(participant)
        if participant.gender == 'F':
            female_time += to_seconds(participant)
    return (male_time/total_male_group, female_time/total_female_group)

def time_by_group(data: dict, group: str)-> tuple:
    new_group = data[group].values()
    total_male_group, total_female_group = sum_time(new_group) 

    return (total_male_group, total_female_group)


def average_time_by_group_and_gender(data: dict):
    # juniors = len(data['junior'])
    # seniors = len((data['senior']))
    # masters = len(data['master'])

    male_junior, female_junior = time_by_group(data, 'junior')
    male_senior, female_senior = time_by_group(data, 'senior')
    male_master, female_master = time_by_group(data, 'master')


    return [ ['juniors', str(datetime.timedelta(seconds=round(male_junior))), str(datetime.timedelta(seconds=round(female_junior)))],
        ['seniors', str(datetime.timedelta(seconds=round(male_senior))), str(datetime.timedelta(seconds=round(female_senior)))],
        ['masters', str(datetime.timedelta(seconds=round(male_master))), str(datetime.timedelta(seconds=round(female_master)))]
    ]
    
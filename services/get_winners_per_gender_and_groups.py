import functools
from helpers.full_name import full_name
from helpers.separate_gender import separate_gender
from helpers.time_helper import check_time


def get_winners_by_gender_and_groups(data) -> tuple:
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
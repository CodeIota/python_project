import datetime
import functools
from helpers.separate_gender import separate_gender
from helpers.time_helper import check_time, to_seconds
from helpers.full_name import full_name


def get_winners_by_gender(data) -> list:
    male_list, female_list = separate_gender(data)
    winner_male = functools.reduce(check_time, male_list)
    winner_female = functools.reduce(check_time, female_list)

    return [['male', full_name(winner_male), str(datetime.timedelta(seconds=to_seconds(winner_male)))],
    ['female', full_name(winner_female), str(datetime.timedelta(seconds=to_seconds(winner_female)))]
    ]
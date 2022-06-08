import datetime
import functools

from helpers.time_helper import check_time, to_seconds
from helpers.full_name import full_name 


def get_winners_by_group(data) -> list:
    junior = data['junior'].values()
    senior = data['senior'].values()
    master = data['master'].values()

    winner_junior = functools.reduce(check_time, junior) 
    winner_senior = functools.reduce(check_time, senior)
    winner_master = functools.reduce(check_time, master)

    return [['junior', full_name(winner_junior), str(datetime.timedelta(seconds=to_seconds(winner_junior)))], 
    ['senior', full_name(winner_senior), str(datetime.timedelta(seconds=to_seconds(winner_senior)))], 
    ['master', full_name(winner_master), str(datetime.timedelta(seconds=to_seconds(winner_master)))]]
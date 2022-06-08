import functools
from helpers.full_name import full_name

from helpers.time_helper import check_time


def get_general_winner(data):
    winner = functools.reduce(check_time, data.values())
    return full_name(winner)
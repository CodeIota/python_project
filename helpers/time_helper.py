
def to_seconds(person)-> int:
    return int(person.seconds) + int(person.minutes)*60 + int(person.hours)* 3600


def check_time(participant1, participant2):
    time_participant1 = to_seconds(participant1)
    time_participant2 = to_seconds(participant2)

    if time_participant2 < time_participant1:
        return participant2
    else: return participant1
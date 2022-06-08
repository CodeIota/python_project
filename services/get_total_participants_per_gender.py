def get_total_participants_by_gender(data: dict) -> tuple:
    total_male, total_female = (0, 0)
    for participant in data:
        if participant.gender == 'M':
            total_male += 1
        if participant.gender == 'F':
            total_female += 1
    return (total_male, total_female)
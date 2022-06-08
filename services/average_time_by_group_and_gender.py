from services.get_total_participants_by_group import get_total_participants_by_group


def gender_by_group(data: dict, group: str)-> tuple:
    group = data[group]
    total_male_group, total_female_group = get_total_participants_by_group(group)

    return (total_male_group, total_female_group)


def average_time_by_group_and_gender(data: dict):
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
    
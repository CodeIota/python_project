from services.get_total_participants_per_group import get_total_participants_by_group


def get_histogram_per_group(data):
    (junior, senior, master) = get_total_participants_by_group(data)

    print('junior(x) | ', '*' * round(junior/5))
    print('senior(y) | ', '*' * round(senior / 5))
    print('master(z) | ', '*' * round(master / 5))
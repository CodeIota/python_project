def get_total_participants_by_group(data: dict)-> tuple:
    juniors = len(data['junior'])
    seniors = len((data['senior']))
    masters = len(data['master'])
    data = (juniors, seniors, masters)
    return data
def separate_gender(data: dict):
    male, female = [], []
    
    for person in data.values():
        if person.gender == 'M':
            male.append(person)
        if person.gender == 'F':
            female.append(person)

    return (male, female)
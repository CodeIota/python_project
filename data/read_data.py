from Person import Person

def get_person_data() -> dict:
    data = {}
    file = open('competencia.txt').readlines()

    for person_key, line in enumerate(file):
        row_data = line.split(',')
        dni, first_lastname, second_lastname, name, initial_second_name, gender, age, hours, minutes, seconds = [i.strip() for i in row_data]
        person = Person(dni, first_lastname, second_lastname, name, initial_second_name, gender, age, hours, minutes, seconds)
        data[person_key] = person
    
    return data

def define_group() -> dict:
    job_group = {'junior': {}, 'senior': {}, 'master': {}}
    persons_dict: dict = get_person_data()
    for key, person in persons_dict.items(): 
        if int(person.age) > 40:
            job_group['master'][key] = person
        if 25 <= int(person.age) <= 40:
            job_group['senior'][key] = person
        if int(person.age) <=25:
            job_group['junior'][key] = person
    return job_group

final_data: dict = define_group()
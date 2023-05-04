import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

django.setup()

if __name__ == '__main__':
    from faker import Faker

    fake = Faker()

    # Generate individuals
    individuals_file = open('individuals_insert.txt', 'w')
    individuals_file.write('INSERT INTO restapi_individuals (firstname, lastname, nationality, age, job) VALUES\n')
    n_individuals = 50000
    for i in range(n_individuals):
        firstname = fake.first_name().replace("'", "")[:25]
        lastname = fake.last_name().replace("'", "")[:25]
        nationality = fake.country().replace("'", "")[:20]
        age = random.randint(18, 90)
        job = fake.job().replace("'", "")[:50]
        values_str = f"('{firstname}', '{lastname}', '{nationality}', {age}, '{job}')"
        if i == n_individuals - 1:
            values_str += ';'
        else:
            values_str += ',\n'
        individuals_file.write(values_str)
    individuals_file.close()

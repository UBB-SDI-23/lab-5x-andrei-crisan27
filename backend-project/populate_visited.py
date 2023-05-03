import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

django.setup()

if __name__ == '__main__':
    from faker import Faker

    fake = Faker()

    # Generate visited countries
    visited_countries_file = open('visited_countries_insert.txt', 'w')
    visited_countries_file.write('INSERT INTO restapi_visitedcountries (individual_id, country_id, year, review) VALUES\n')
    n_visited_countries = 100000
    for i in range(n_visited_countries):
        year = random.randint(2000, 2022)
        review = fake.sentence(nb_words=10)
        values_str = f"({i}, {100000}, {year}, '{review}')"
        if i == n_visited_countries - 1:
            values_str += ';'
        else:
            values_str += ',\n'
        visited_countries_file.write(values_str)
    visited_countries_file.close()

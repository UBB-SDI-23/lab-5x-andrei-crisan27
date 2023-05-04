import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

django.setup()

from faker import Faker


if __name__ == '__main__':
    fake = Faker()
    n = 50000
    file = open('companies_insert.txt', 'w')
    file.write('INSERT INTO restapi_companies (name, year_founded, number_of_employees, country_id, activity, text_field) VALUES\n')

    for i in range(n):
        company_name = f"{fake.company()} {random.randint(1, 100)}"[:25]
        company_name = company_name.replace("'", "")
        year_founded = fake.random_int(min=1900, max=2022)
        number_of_employees = fake.random_int(min=1, max=10000)
        country_id = random.randint(1, 200000)
        activity = fake.word(ext_word_list=['Consulting', 'Technology', 'Manufacturing', 'Retail', 'Finance', 'Transportation'])[:50]
        text_field = fake.lorem.words(nb=100, ext_word_list=None, unique=False)

        values_str = f"('{company_name}', {year_founded}, {number_of_employees}, {country_id}, '{activity}', '{text_field}')"
        if i == n - 1:
            values_str += ';'
        else:
            values_str += ',\n'
        file.write(values_str)

    file.close()

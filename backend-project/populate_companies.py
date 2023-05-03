# name = models.CharField(max_length=25)
# year_founded = models.IntegerField(validators=[validate_year_founded])
# number_of_employees = models.IntegerField()
# country = models.ForeignKey(Countries, on_delete=models.CASCADE)
# activity = models.CharField(max_length=50)

import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

django.setup()

from django.core.exceptions import ObjectDoesNotExist
from faker import Faker

from restapi.models import Company, Countries
from restapi.validators import validate_year_founded


if __name__ == '__main__':
    fake = Faker()
    n = 100000
    file = open('companies_insert.txt', 'w')
    file.write('INSERT INTO restapi_company (name, year_founded, number_of_employees, country_id, activity) VALUES\n')

    for i in range(n):
        company_name = f"{fake.company()} {random.randint(1, 100)}"[:25]
        company_name = company_name.replace("'", "")
        year_founded = fake.random_int(min=1900, max=2022)
        number_of_employees = fake.random_int(min=1, max=10000)
        country_id = random.randint(1, 1000000)
        activity = fake.word(ext_word_list=['Consulting', 'Technology', 'Manufacturing', 'Retail', 'Finance', 'Transportation'])[:50]

        values_str = f"('{company_name}', {year_founded}, {number_of_employees}, {country_id}, '{activity}')"
        if i == n - 1:
            values_str += ';'
        else:
            values_str += ',\n'
        file.write(values_str)

    file.close()

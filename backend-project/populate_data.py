import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

django.setup()

# name = models.CharField(max_length=25)
# continent = models.CharField(max_length=25, validators=[validate_continent])
# population = models.IntegerField()
# capital = models.CharField(max_length=25)
# surface = models.IntegerField()


if __name__ == '__main__':
    from faker import Faker

    file = open('countries_insert.txt', 'w')
    file.write('INSERT INTO restapi_countries (name, continent, population, capital, surface) VALUES\n')

    fake = Faker()
    n = 100
    for i in range(n):
        country_name = f"{fake.country()} {random.randint(1, 100)}"[:25]
        country_name = country_name.replace("'", "")
        continent = fake.word(
            ext_word_list=['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'])[:25]
        population = fake.random_int(min=0, max=10000)
        capital = fake.city()[:25]
        capital = capital.replace("'", "")
        surface = fake.random_int(min=0, max=10000)

        values_str = f"('{country_name}', '{continent}', {population}, '{capital}', {surface})"
        if i == n - 1:
            values_str += ';'
        else:
            values_str += ',\n'
        file.write(values_str)

    file.close()

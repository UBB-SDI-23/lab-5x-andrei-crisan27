import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

django.setup()


from restapi.models import Countries
import pycountry
from geonamescache import GeonamesCache

gc = GeonamesCache()
cities = [city['name'] for city in gc.get_cities()]

countries = list(pycountry.countries)



if __name__ == '__main__':
    from faker import Faker

    fake = Faker()
    n = 100
    for _ in range(n):
        Countries.objects.create(name=random.choice(countries)+str(random.randint(0, 10000)), continent=fake.name()[0]+str(random.randint(0, 10000)), population=random.randint(0, 1000), capital=random.choice(cities), surface=random.randint(0, 1000))


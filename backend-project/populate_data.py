import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

django.setup()


from restapi.models import Countries
import pycountry
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-app")

# Get the top 1000 cities by population
location_list = geolocator.geocode("country", exactly_one=False, limit=1000)

# Extract the city names from the locations
cities = [location.address.split(", ")[0] for location in location_list]

countries = list(pycountry.countries)



if __name__ == '__main__':
    from faker import Faker

    fake = Faker()
    n = 100
    for _ in range(n):
        Countries.objects.create(name=random.choice(countries)+str(random.randint(0, 10000)), continent=fake.name()[0]+str(random.randint(0, 10000)), population=random.randint(0, 1000), capital=random.choice(cities), surface=random.randint(0, 1000))


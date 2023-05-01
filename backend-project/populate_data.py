import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings')

django.setup()


from restapi.models import Countries
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
             'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
             'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
             'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada',
             'Central African Republic (CAR)', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
             'Democratic Republic of the Congo', 'Republic of the Congo', 'Costa Rica', 'Cote dIvoire', 'Croatia',
             'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
             'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France',
             'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
             'Guinea - Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
             'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
             'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
             'Liechtenstein',
             'Lithuania', 'Luxembourg', 'Macedonia(FYROM)', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
             'Malta',
             'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
             'Montenegro', 'Morocco', 'Mozambique', 'Myanmar(Burma)',
             'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea',
             'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
             'Philippines',
             'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
             'Saint Vincent and the Grenadines',
             'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
             'Sierra Leone', 'Singapore',
             'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan',
             'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland',
             'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of',
             'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
             'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
             'United Kingdom of Great Britain and Northern Ireland', 'United States Minor Outlying Islands',
             'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of',
             'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Western Sahara',
             'Yemen', 'Zambia', 'Zimbabwe']

continents = ['Europe', 'Asia', 'Africa', 'Antarctica', 'North America', 'South America', 'Australia', 'Oceania']

# name = models.CharField(max_length=25)
# continent = models.CharField(max_length=25, validators=[validate_continent])
# population = models.IntegerField()
# capital = models.CharField(max_length=25)
# surface = models.IntegerField()


if __name__ == '__main__':
    from faker import Faker

    file = open('countries_insert.txt', 'w')
    file.write('INSERT INTO restapi_countries VALUES')

    fake = Faker()
    n = 100
    for _ in range(n):
        # Countries.objects.create(name=str(random.choice(countries)) + str(random.randint(0, 1000)),
        #                          continent=str(random.choice(continents)) + str(random.randint(0, 10000)),
        #                          population=random.randint(0, 1000), capital=fake.name()[:3],
        #                          surface=random.randint(0, 1000))
        file.write(f"('{str(random.choice(countries)) + str(random.randint(0, 1000))}','{str(random.choice(continents)) + str(random.randint(0, 10000))}', {random.randint(0, 1000)}, '{fake.name()[:3] + str(random.randint(0, 1000))}', {random.randint(0, 1000)}),")
import json

import Airport as Airport
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Demo command'

    def handle(self, *args, **options):
        # airport = Airport(
        #     code='ADL',
        #     name='Adelaide International Airport',
        #     country='Australia',
        #     city='Adelaide',
        #     length=10171
        # )
        # print(airport)
        # airport.save()
        # print(airport)
        airport = Airport.objects.create(
            code="DUS",
            name="Dusseldorf International Airport",
            country="Germany",
            city="Dusseldorf",
            length=9842
        )
        airport = Airport.objects.create(
            code="ARH",
            name="Arkhangelsk Airport",
            country="Russia",
            city="Arkhangelsk",
            length=8202.1
        )
        print(airport)

        airports = Airport.objects.all()
        print(airports)

        airport = Airport.objects.filter(id=2)
        print(airport)

        airport = Airport.objects.filter(length__gte=9000)
        print(airport)

        try:
            airport = Airport.objects.get(code='DUS')
        except Airport.DoesNotExist:
            print('=(')

        airport.length += 1000
        airport.save()

        res = Airport.objects.update(country='Russia')
        print(res)

        with open('airports.json') as file:
            airports_data = json.load(file)
        print(airports_data)

        for airport_data in airports_data:
            airport = Airport.objects.create(
            code=airport_data['code'],
            name=airport_data['name'],
            country=airport_data['country'],
            city=airport_data['city'],
            length=airport_data['length']
        )
        print(airport)




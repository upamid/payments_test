import json
import os

from django.core.management import BaseCommand

from bill.models import Service

fixture_dir = ''
fixture_filename = 'services.json'


class Command(BaseCommand):
    help = "load data"

    def handle(self, *args, **options):
        fixture_file = os.path.join(fixture_dir, fixture_filename)
        print(fixture_file)
        f = open(fixture_file, encoding="utf8")
        my_json_obj = json.load(f)
        for title in my_json_obj:
            Service.objects.create(
                name = title['name'],
                price = title['price']
                )
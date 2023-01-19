import csv
import pytz
from django.conf import settings
from django.core.management.base import BaseCommand
# from weather.forms import WeatherForm
from geos.models import Community
from geos.models import CommunityType
from geos.models import Parish
from django.db import transaction

# use this to run custom command --> python manage.py import_excel D:\development\GEO_dm\settlements.csv
class Command(BaseCommand):
    help = 'imports information from "settlements.csv" file'

    def add_arguments(self, parser):
        parser.add_argument('input_path')

    @transaction.atomic
    def handle(self, *args, **options):
        with transaction.atomic():

            input_path = options['input_path']
            with open(input_path, 'r') as f_input:
                reader = csv.DictReader(f_input)

                for row in reader:
                    name = row['name'].strip()
                    parish_name = row['parish'].strip()
                    parish_code = row['code'].strip().upper()
                    type_name = row['type'].strip().lower()
                    longitude = row['longitude'].strip()
                    latitiude = row['latitude'].strip()

                    parish, _ = Parish.objects.get_or_create(
                        code=parish_code,

                        defaults={
                            'code': parish_code,
                            'name': parish_name,
                        }
                    )

                    type, _ = CommunityType.objects.get_or_create(
                        name__iexact=type_name,

                        defaults={
                            'name': type_name,
                        }
                    )

                    community, community_created = Community.objects.update_or_create(
                        parish=parish,
                        name__iexact=name,

                        defaults={
                            'type': type,
                            'name': name,
                            'lng': longitude,
                            'lat': latitiude,
                        }
                    )
                    print('+' if community_created else '-', community, parish, type, parish_code)
                pass
            return
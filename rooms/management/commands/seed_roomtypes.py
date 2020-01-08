from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Seed(object):
    instance = None
    seeders = {}
    fakers = {}

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Seed, cls).__new__(*args, **kwargs)
        return cls.instance

    def __init__(self):
        pass

    @staticmethod
    def codename(locale=None):
        from django.conf import settings
        locale = locale or getattr(settings, 'LANGUAGE_CODE', None)
        codename = locale or 'default'
        return codename

    @classmethod
    def faker(cls, locale=None, codename=None):
        code = codename or cls.codename(locale)
        if code not in cls.fakers:
            from faker import Faker
            cls.fakers[code] = Faker(locale)
            cls.fakers[code].seed_instance(random.randint(1, 10000))
        return cls.fakers[code]

    @classmethod
    def seeder(cls, locale=None):
        code = cls.codename(locale)
        if code not in cls.seeders:
            faker = cls.fakers.get(code, None) or cls.faker(codename=code)
            from django_seed import seeder
            cls.seeders[code] = seeder.Seeder(faker)

        return cls.seeders[code]


class Command(BaseCommand):

    help = "This command creates amenities"

    """ def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )   """

    def handle(self, *args, **options):
        room_type = ["Entire place", "Private room", "Shared room", "Hotel"]
        for t in room_type:
            RoomType.objects.create(name=t)
        self.stdout.write(self.style.SUCCESS(f"{len(room_type)} room types created!"))

import random
from django.core.management.base import BaseCommand
# from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models


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

    help = "This command creates many reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews do you want to create")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(review_models.Review, number, {
            "accuracy": lambda x: random.randint(0, 6),
            "communication": lambda x: random.randint(0, 6),
            "cleanLiness": lambda x: random.randint(0, 6),
            "location": lambda x: random.randint(0, 6),
            "check_in": lambda x: random.randint(0, 6),
            "value": lambda x: random.randint(0, 6),
            "room": lambda x: random.choice(rooms),
            "user": lambda x: random.choice(users),
        },)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} review created!"))

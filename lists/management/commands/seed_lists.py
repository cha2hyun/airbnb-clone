# import random
# from django.core.management.base import BaseCommand
# from django.contrib.admin.utils import flatten
# from django_seed import Seed
# from lists import models as list_models
# from users import models as user_models
# from rooms import models as room_models

# NAME = "lists"

# class Command(BaseCommand):

#     help = f"This command creates many {NAME}"

#     def add_arguments(self, parser):
#         parser.add_argument(
#             "--number", default=2, type=int, help=f"How many {NAME} do you want to create")

#     def handle(self, *args, **options):
#         number = options.get("number")
#         seeder = Seed.seeder()
#         users = user_models.User.objects.all()
#         rooms = room_models.Room.objects.all()
#         seeder.add_entity(list_models.List, number, {
#             "user": lambda x: random.choice(users),
#         },)

#         created = seeder.execute()
#         cleaned = flatten(list(created.values()))
#         for pk in cleaned:
#             list_model = list_models.List.objects.get(pk=pk)
#             to_add = rooms[random.randint(0, 5):random.randint(6, 30)]
#             list_model.rooms.add(*to_add)

#         self.stdout.write(self.style.SUCCESS(f"{number} {NAME} Created!"))

import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
# from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models


NAME = "lists"


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

    help = f"This command creates {NAME}"

    def handle(self, *args, **options):
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        for user in users:
            list_model = list_models.List.objects.create(user=user, name="Favs.")
            to_add = rooms[random.randint(0, 5): random.randint(6, 30)]
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(f"{0} {NAME} created!"))

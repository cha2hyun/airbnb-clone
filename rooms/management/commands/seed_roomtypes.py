from django.core.management.base import BaseCommand
from rooms.models import RoomType


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
        
import random
from django.core.management.base import BaseCommand
from _2_app.models import Trow


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Numder of trows')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        result = Trow.last_trow(count)
        self.stdout.write(f"{count}, {result}")
import random
from django.core.management.base import BaseCommand
from _2_app.models import Trow


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        trow = Trow(result_of_trow=random.choice(Trow.RESULT_OF_TROW)[0])
        trow.save()
        self.stdout.write(f"{trow}")

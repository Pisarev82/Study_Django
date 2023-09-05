from datetime import datetime
import random
from django.core.management.base import BaseCommand
from _2_app.models import Author


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            author = Author(
                name=f"name_{i}",
                surname=f"surname_{i}",
                email=f"email_{i}@email.ru",
                biography=f"biography_{i}",
                birthday=f"{datetime.today()}"
            )

            author.save()
            self.stdout.write(f"{author}")
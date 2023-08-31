import random
import django.utils.timezone as timezone
from collections import deque
from django.db import models



# Create your models here.
class Trow(models.Model):
    HEADS = "heads"
    TAILS = "tails"

    RESULT_OF_TROW = (
        ((HEADS, "heads"), (TAILS, "tails"))
    )

    result_of_trow = models.CharField(choices=RESULT_OF_TROW, max_length=7)
    trow_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.result_of_trow}, {self.trow_time}'

    #Логику прописовать в модели тупо. Нужно перенести во views
    @staticmethod
    def last_trow(count_trow):
        result = {Trow.HEADS: 0, Trow.TAILS: 0}
        data = reversed(deque(Trow.objects.all().order_by('id'), maxlen=count_trow))
        for i in data:
            print(i)
            choice_result_trow = random.choice(Trow.RESULT_OF_TROW)
            result[choice_result_trow[0]] += 1
        return result


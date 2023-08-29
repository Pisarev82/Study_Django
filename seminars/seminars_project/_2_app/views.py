import random
from random import randint
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def choice(request):
    to_choice = ["Орел", "Решка"]
    return HttpResponse(f'{random.choice(to_choice)}')


def cube(request):
    return HttpResponse(f"{randint(1,6)}")


def rand100(request):
    result = randint(1,100)
    logger.info(f"_2_app def rand100 {result}")
    return HttpResponse(f"{result}")
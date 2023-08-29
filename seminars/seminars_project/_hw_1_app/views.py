import random
from datetime import datetime
from random import randint
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def main(request):
    logger.info(f"_hw_1_app def main at {datetime.now()}")
    return HttpResponse(f'<h1>Главная страница</h1> <p>Очень важная информация на главной странице</p>')


def about(request):
    logger.info(f"_hw_1_app def about at {datetime.now()}")
    return HttpResponse(f'<h1>Создатель</h1> <p>Писарев Николай</p> <p>Junior Django developer</p>')


def rand100(request):
    result = randint(1,100)
    logger.info(f"_2_app def rand100 {result}")
    return HttpResponse(f"{result}")
import random
from datetime import datetime
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)
#23:05

def main(request):
    logger.info(f"_hw_1_app def main at {datetime.now()}")
    context = {'name': "Nikolay", 'title': 'Main', }
    return render(request, '_hw_1_app/choice.html', context)


def about(request):
    logger.info(f"_hw_1_app def about at {datetime.now()}")

    context = {'dataTime': datetime.now(),
               'client_ip': get_client_ip(request),
               'title': 'About',
               }

    return render(request, '_hw_1_app/about.html', context)


def rand100(request):
    result = randint(1,100)
    logger.info(f"_2_app def rand100 {result}")
    return HttpResponse(f"{result}")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # Если ip передан через proxy
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip
    # Если открыто
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

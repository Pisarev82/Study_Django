from django.shortcuts import render
from .models import *

def get_orders(request, client_id):
    orders = Order.objects.filter(order__pk=client_id)
    context = {'orders': orders, 'title': 'orders', }
    return render(request, 'online_store/orders.html', context)

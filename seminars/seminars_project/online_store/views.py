from django.core.files.storage import FileSystemStorage

from . import forms
from django.shortcuts import render, get_object_or_404
from .models import *
from datetime import datetime, timedelta


def get_orders(request, client_id):

    client = get_object_or_404(Client, pk=client_id)
    orders = client.order_set.all()

    context = {
        'title': 'articles',
        'client': client,
        'orders': orders,

    }

    return render(request, 'online_store/orders.html', context)


def list_client_items(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    period = request.GET.get('period')
    selected_period = int(period) if period else None

    if selected_period == 7:
        date_from = datetime.now() - timedelta(days=7)
    elif selected_period == 30:
        date_from = datetime.now() - timedelta(days=30)
    elif selected_period == 365:
        date_from = datetime.now() - timedelta(days=365)
    else:
        date_from = None

    if date_from:
        items = OrderItem.objects.filter(
            order__customer=client,
            order__date_ordered__gte=date_from,
        ).order_by('-order__date_ordered')
    else:
        items = None

    context = {
        'client': client,
        'items': items,
        'selected_period': selected_period,
    }

    return render(request, 'online_store/client.html', context)


def add_image_product(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    if request.method == 'POST':
        form = forms.AddImageProduct(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']

            product.photo = photo
            product.save()
    else:
        form = forms.AddImageProduct()

    return render(request, 'online_store/add_image_product.html', {'form': form})


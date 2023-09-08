from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:client_id>', views.get_orders, name='orders')
    # path('about/', views.about, name='about'),
]

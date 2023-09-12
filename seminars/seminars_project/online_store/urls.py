from django.urls import path
from . import views


urlpatterns = [
    path('orders/<int:client_id>', views.get_orders, name='orders'),
    path('client/<int:client_id>/items/', views.list_client_items, name='list_client_items'),
path('add_image_product/<int:product_id>', views.add_image_product, name='add_image_product'),
]

from django.contrib import admin
from .models import Client, Product, Order, OrderItem


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'date_registered')
    list_filter = ('date_registered',)
    search_fields = ('name', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'added_date')
    list_filter = ('added_date',)
    search_fields = ('name', 'description')
    list_editable = ('price', 'quantity')  # Редактируемая цена и количество на списке


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'date_ordered')
    list_filter = ('date_ordered',)
    search_fields = ('customer__name',)
    filter_horizontal = ('products',)  # Улучшенный вид для выбора продуктов


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')
    list_filter = ('order__date_ordered',)
    search_fields = ('product__name', 'order__customer__name')
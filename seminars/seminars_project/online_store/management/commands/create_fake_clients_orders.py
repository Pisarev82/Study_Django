
import random
from django.core.management.base import BaseCommand
import random
import faker
from django.utils import timezone
from online_store.models import Client, Product, Order, OrderItem


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = faker.Faker()
        for i in range(10):
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            address = fake.address()
            date_registered = timezone.now() - timezone.timedelta(days=random.randint(1, 365))

            client = Client.objects.create(
                name=name,
                email=email,
                phone_number=phone,
                address=address,
                date_registered=date_registered
            )
            client.save()

        # Создать 10 фейковых товаров
        for i in range(10):
            name = fake.word()
            description = fake.sentence()
            price = round(random.uniform(10, 100), 2)
            quantity = random.randint(1, 100)
            added_date = timezone.now() - timezone.timedelta(days=random.randint(1, 365))

            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                added_date=added_date
            )
            product.save()

        # Создать 10 фейковых заказов
        clients = Client.objects.all()
        products = Product.objects.all()

        for i in range(10):
            customer = clients[random.randrange(0, len(clients))]
            order = Order.objects.create(customer=customer, total_price=0)

            # Добавить случайное количество случайных товаров в заказ
            for j in range(random.randint(1, len(products))):
                product = products[random.randrange(0, len(products))]
                price = product.price
                quantity = random.randint(1, 10)
                OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

                # Обновить общую сумму заказа
                order.total_price += price * quantity
            order.save()
        self.stdout.write(f"mission complite")



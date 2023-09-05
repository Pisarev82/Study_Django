from datetime import datetime
import random
from django.core.management.base import BaseCommand
from _2_app.models import Author
from django.utils import timezone
from faker import Faker
from _2_app.models import Article


class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument('num_articles', type=int, help='Numder of articles')

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_articles = kwargs['num_articles']
        for _ in range(num_articles):
            title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            content = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
            publication_date = fake.date_time_between(start_date='-1y', end_date='now',
                                                      tzinfo=timezone.get_current_timezone())
            author = Author.objects.order_by('?').first()
            category = fake.word()
            views = random.randint(0, 100)
            is_published = fake.boolean(chance_of_getting_true=80)

            article = Article.objects.create(
                title=title,
                content=content,
                publication_date=publication_date,
                author=author,
                category=category,
                views=views,
                is_published=is_published
            )

            article.save()
            self.stdout.write(f"{article}")



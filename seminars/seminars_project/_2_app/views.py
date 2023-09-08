import random
from random import randint
from django.http import HttpResponse
import logging

from django.shortcuts import render
from .models import Author, Article, Comment

logger = logging.getLogger(__name__)


# Create your views here.
def choice(request):
    to_choice = ["Орел", "Решка"]
    result = f'{random.choice(to_choice)}'
    context = {'choice': result, 'title': 'choice', }
    return render(request, '_2_app/choice.html', context)



def cube(request):
    result = f"{randint(1,6)}"
    context = {'choice': result, 'title': 'choice', }
    return render(request, '_2_app/choice.html', context)


def rand100(request):
    result = randint(1,100)
    context = {'choice': result, 'title': 'choice', }
    return render(request, '_2_app/choice.html', context)


def get_articles(request, author_id):
    articles = Article.objects.filter(author__pk=author_id)
    context = {'articles': articles, 'title': 'articles', }
    return render(request, '_2_app/articles.html', context)


def get_article(request, article_id):
    article = Article.objects.filter(pk=article_id).first()
    article.views += 1
    article.save()
    context = {'article': article, 'title': 'article', }
    return render(request, '_2_app/article.html', context)

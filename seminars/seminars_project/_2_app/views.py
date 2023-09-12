import random
from random import randint
from django.http import HttpResponse
import logging
from . import forms

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


def game(request):
    if request.method == 'POST':
        form = forms.ChoiceForm(request.POST)
        if form.is_valid():
            g = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if g == 'd':
                return cube(request)
            elif g == 'r':
                return rand100(request)
            elif g == 'c':
                return choice(request)
    else:
        form = forms.ChoiceForm()

    return render(request, '_2_app/game.html', {'form': form})


def add_author(request):
    message = "Заполните все поля"
    if request.method == 'POST':
        form = forms.AddAuthor(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(name=name,
                            surname=surname,
                            email=email,
                            biography=biography,
                            birthday=birthday)
            author.save()
            message = "Автор успешно сохранен"
    else:
        form = forms.AddAuthor()

    return render(request, '_2_app/addauthor.html', {'form': form, 'message': message})


def add_article(request):
    message = "Заполните все поля"
    if request.method == 'POST':
        form = forms.Article(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']

            article = Article(title=title,
                            content=content,
                            author=author,
                            category=category)
            article.save()
            message = "Статья успешно сохранен"
    else:
        form = forms.Article()

    return render(request, '_2_app/addarticle.html', {'form': form, 'message': message})


def comment_form(request, article_id):
    message = ""
    article = Article.objects.filter(pk=article_id).first()
    comments = Comment.objects.filter(article=article_id).all()
    if request.method == 'POST':
        form = forms.Comment(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            author = form.cleaned_data['author']

            comment = Comment(
                            comment=comment,
                            author=author,
                            article=article,
                            )
            comment.save()
            message = "Коментарий успешно сохранен"

    else:
        form = forms.Comment()

    return render(
        request,
        '_2_app/article_with_comment.html',
        {
            'form': form,
            'message': message,
            'title': "Статья с возможностю коментировать",
            'article': article,
            'comments': comments
        })


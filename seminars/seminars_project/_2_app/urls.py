
from django.urls import path
from . import views

urlpatterns = [
    path('choice/', views.choice, name='choice'),
    path('cube/', views.cube, name='cube'),
    path('rand100/', views.rand100, name='rand100'),
    path('articles/<int:author_id>', views.get_articles, name='articles'),
    path('article/<int:article_id>', views.get_article, name='article'),
    path('game/', views.game, name='game'),
    path('addauthor/', views.add_author, name='addauthor'),
    path('addarticle/', views.add_article, name='addarticle'),
    path('article_with_comment/<int:article_id>', views.comment_form, name='article_with_comment'),
]
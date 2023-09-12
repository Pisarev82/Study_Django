import datetime
from _2_app import models
from django import forms


class ChoiceForm(forms.Form):
    game = forms.ChoiceField(choices=[
        ('d', 'dice'),
        ('r', 'Случайное число'),
        ('c', 'монетка')])
    count = forms.IntegerField(min_value=1, max_value=64)


class AddAuthor(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Фамилия', max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField(
        initial=datetime.date.today(),
        widget=forms.DateInput(attrs={'type': 'date'})
    )


class Article(forms.Form):
    title = forms.CharField(label='Название', max_length=200)
    content = forms.CharField(label='Текст статьи', widget=forms.Textarea)
    # author = forms.ChoiceField(
    #     label='Автор',
    #     choices=[(author.id, str(author)) for author in models.Author.objects.all()]
    # )
    author = forms.ModelChoiceField(label='Автор', queryset=models.Author.objects.all())
    category = forms.CharField(label='Категория', max_length=100)
    # is_published = forms.BooleanField(label='опубликовать', )


class Comment(forms.Form):
    author = forms.ModelChoiceField(label='Автор', queryset=models.Author.objects.all())
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)

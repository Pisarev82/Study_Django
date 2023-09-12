
from online_store import models
from django import forms


class AddImageProduct(forms.Form):
    photo = forms.ImageField()


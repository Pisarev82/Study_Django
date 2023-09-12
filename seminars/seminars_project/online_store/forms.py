
from online_store import models
from django import forms


class add_image_product(forms.Form):
    photo = forms.ImageField()


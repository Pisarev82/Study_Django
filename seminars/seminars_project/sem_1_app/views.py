from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('<img src="https://media.tenor.com/kT5Er1ugzHsAAAAd/cat.gif" width="518" height="541.6993464052288" alt="Cat GIF - Cat GIFs" style="max-width: 518px;">')


def about(request):
 return HttpResponse("About us")


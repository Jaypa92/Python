from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return httpResponse("<h1>Learning Django!!</h1>")
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
     return HttpResponse('Hello World')

def item(request):
     return HttpResponse('<h1>This is the item view</h1>')
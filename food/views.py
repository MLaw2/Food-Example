from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def item(request):
    return HttpResponse('This is an item view')

def hahafard(request):
    return HttpResponse('mlaw2.github.io')
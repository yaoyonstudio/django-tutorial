from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, django!')

def index(request):
    context = { 'title': 'Django Tutorial' }
    return render(request, 'home/index.html', context)
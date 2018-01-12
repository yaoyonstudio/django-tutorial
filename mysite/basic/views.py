from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = { 'title': '环境搭建与项目初始化 ' }
    return render(request, 'basic/index.html', context)

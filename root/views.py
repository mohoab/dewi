from django.shortcuts import render
from .models import *

def homepage(request):
    que = Question.objects.filter(status=True)[:4]
    services = Service.objects.filter(status=True)[:6]
    contexts = {
        'questions': que ,
        'services': services

    }
    return render(request,'root/index.html',context=contexts)
def inner(request):
    return render(request,'root/inner-page.html')
def products(request):
    return render(request,'root/courses.html')
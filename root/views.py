from django.shortcuts import render
from .models import Question,Service,Product,Info
from django.contrib.auth.models import User

def homepage(request):
    que = Question.objects.filter(status=True)[:4]
    services = Service.objects.filter(status=True)[:6]
    products_number = Product.objects.filter(status=True).count()
    products = Product.objects.all()
    info = Info.objects.all()
    user_c = User.objects.all().count()
    contexts = {
        'questions': que ,
        'services': services,
        'p_number':products_number , 
        'products': products ,
        'info': info ,
        'uc' : user_c ,
        

    }
    return render(request,'root/index.html',context=contexts)
def inner(request):
    return render(request,'root/inner-page.html')
def products(request):
    return render(request,'root/courses.html')
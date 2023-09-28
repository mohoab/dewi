from django.shortcuts import render
from .models import Question,Service,Product,Info,About,Future,Brand,Contact
from django.contrib.auth.models import User

def homepage(request):
    que = Question.objects.filter(status=True)[:4]
    services = Service.objects.filter(status=True)[:6]
    products_number = Product.objects.filter(status=True).count()
    products = Product.objects.all()
    info = Info.objects.all()[:1]
    user_c = User.objects.all().count()
    about=About.objects.filter(status=True)[:1]
    future = Future.objects.filter(status=True)[:3]
    brand = Brand.objects.filter(status=True)[:8]
    contact = Contact.objects.filter(status=True)[:1]
    contexts = {
        'questions': que ,
        'services': services,
        'p_number':products_number , 
        'products': products ,
        'info': info ,
        'uc' : user_c ,
        'about': about ,
        'future' : future , 
        'brand' : brand , 
        'contact' : contact ,
    }
    return render(request,'root/index.html',context=contexts)
def inner(request):
    return render(request,'root/inner-page.html')
def products(request):
    product= Product.objects.filter(status=True)
    contexts = {
        'product': product
    }
    return render(request,'root/courses.html',context=contexts )
from django.shortcuts import render
from .models import Question,Service,Product,Info,About,Future,Brand,Contact,Category,Deepcat
from django.contrib.auth.models import User
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def homepage(request):
    que1 = Question.objects.filter(status=True)[0:1]
    que2 = Question.objects.filter(status=True)[1:2]
    que3 = Question.objects.filter(status=True)[2:3]
    que4 = Question.objects.filter(status=True)[3:4]
    services = Service.objects.filter(status=True)[:6]
    products_number = Product.objects.filter(status=True).count()
    products = Product.objects.all()
    info = Info.objects.all()[:1]
    user_c = User.objects.all().count()
    about=About.objects.filter(status=True)[:1]
    future = Future.objects.filter(status=True)[:3]
    brand = Brand.objects.filter(status=True)[:7]
    contact = Contact.objects.filter(status=True)[:1]
    category = Category.objects.filter(status=True)
    deep_cat = Deepcat.objects.filter(status=True)
    last_three = Product.objects.filter(status=True)[:3]
    contexts = {
        'que1': que1 ,
        'que2':que2,
        'que3':que3,
        'que4':que4,
        'services': services,
        'p_number':products_number , 
        'products': products ,
        'info': info ,
        'uc' : user_c ,
        'about': about ,
        'future' : future , 
        'brand' : brand , 
        'contact' : contact ,
        'category' : category ,
        'deep_cat' : deep_cat ,
        'last_three':last_three,
        

    }
    return render(request,'root/index.html',context=contexts)
def products(request,cat=None,decat=None):
    if cat :
        product= Product.objects.filter(category__title=cat,status=True)
    elif decat :
        product= Product.objects.filter(deepcat__id=decat,status=True)
    else:
          product= Product.objects.filter(status=True)
    category = Category.objects.filter(status=True)
    deep_cat = Deepcat.objects.filter(status=True)
    product = Paginator(product ,3)
    first_page=1
    last_page=product.num_pages
    contact = Contact.objects.filter(status=True)[:1]
    try :
        page_number = request.GET.get('page')
        product = product.get_page(page_number)
    except EmptyPage:
            course = course.get_page(1) 

    except PageNotAnInteger:
            product = product.get_page(1) 

    
    contexts = {
        'products': product ,
        'category' : category ,
        'first_page':first_page,
        'last_page': last_page ,
        'deep_cat' : deep_cat , 
        'contact' : contact,
        

    }
    return render(request,'root/courses.html',context=contexts )
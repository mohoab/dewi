from django.shortcuts import render
from .models import Question,Service,Product,Info,About,Future,Brand,Contact,Category
from django.contrib.auth.models import User
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

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
    category = Category.objects.filter(status=True)
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
        'category' : category ,

    }
    return render(request,'root/index.html',context=contexts)
def products(request):
    product= Product.objects.filter(status=True)
    category = Category.objects.filter(status=True)
    product = Paginator(product ,1)
    first_page=1
    last_page=product.num_pages
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

    }
    return render(request,'root/courses.html',context=contexts )
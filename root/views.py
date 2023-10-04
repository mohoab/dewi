from django.shortcuts import  render , redirect
from .models import Question,Service,Product,Info,About,Future,Brand,Contact,Category,Deepcat,Newsletter
from accounts.models import Customeuser
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import NewsletterForm , ContectForm
from django.contrib import messages 

def homepage(request):
    if request.method == 'GET':
        
        que1 = Question.objects.filter(status=True)[0:1]
        que2 = Question.objects.filter(status=True)[1:2]
        que3 = Question.objects.filter(status=True)[2:3]
        que4 = Question.objects.filter(status=True)[3:4]
        ser1 = Service.objects.filter(status=True)[:1]
        ser2 = Service.objects.filter(status=True)[1:3]
        ser3 = Service.objects.filter(status=True)[3:6]
        products_number = Product.objects.filter(status=True).count()
        products = Product.objects.all()
        info = Info.objects.all()[:1]
        user_c = Customeuser.objects.all().count()
        about=About.objects.filter(status=True)[:1]
        future = Future.objects.filter(status=True)[:3]
        brand = Brand.objects.filter(status=True)[:7]
        contact = Contact.objects.filter(status=True)[:1]
        category = Category.objects.filter(status=True)
        category5 = Category.objects.filter(status=True)[:5]
        deep_cat = Deepcat.objects.filter(status=True)
        last_three = Product.objects.filter(status=True)[:3]
        contexts = {
            'que1': que1 ,
            'que2':que2,
            'que3':que3,
            'que4':que4,
            'ser1': ser1,
            'ser2': ser2,
            'ser3': ser3,
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
            'category5':category5 ,
            
            

        }
        return render(request,'root/index.html',context=contexts)
    elif request.method == 'POST' and len(request.POST) ==2 :
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submitted successfully')
            return redirect('root:home')
        else:
            messages.add_message(request,messages.ERROR,'your email invalid')
            return redirect('root:home')
    elif request.method == 'POST' and len(request.POST) > 2 :
        form = ContectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your message was sent')
            return redirect('root:home')
        else:
            messages.add_message(request,messages.ERROR,'your message isnot true')
            return redirect('root:home')
              
    

def products(request,cat=None,decat=None):
    if request.method == 'GET':
        if cat :
            product= Product.objects.filter(category__title=cat,status=True)
        elif decat :
            product= Product.objects.filter(deepcat=decat,status=True)
        else:
            product= Product.objects.filter(status=True)
        category5 = Category.objects.filter(status=True)[:5]    
        category = Category.objects.filter(status=True)
        deep_cat = Deepcat.objects.filter(status=True)
        contact = Contact.objects.filter(status=True)[:1]
        pageinator = Paginator(product,3)
        first_page=1
        last_page=pageinator.num_pages
        
        try :
            page_number = request.GET.get('page')
            page_obj = pageinator.get_page(page_number)
        except EmptyPage:
                page_obj = pageinator.get_page(1) 

        except PageNotAnInteger:
                page_obj = pageinator.get_page(1) 

        
        contexts = {
            'pageinator':pageinator , 
            'products': product ,
            'category' : category ,
            'first_page':first_page,
            'last_page': last_page ,
            'deep_cat' : deep_cat , 
            'contact' : contact,
            'page_obj' : page_obj, 
            'category5': category5,

            

        }
        return render(request,'root/courses.html',context=contexts )
    elif request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submitted successfully')
            return redirect('root:products')
        else:
            messages.add_message(request,messages.ERROR,'your email invalid')
            return redirect('root:products')



def details(request,id=None):
    if request.method == 'GET':
        if id :
            try:
                product= Product.objects.get(id=id)
                category = Category.objects.filter(status=True)
                category5 = Category.objects.filter(status=True)[:5]
                deep_cat = Deepcat.objects.filter(status=True)
                contact = Contact.objects.filter(status=True)[:1]
                context={
                    'pr':product,
                    'deep_cat':deep_cat,
                    'category':category,
                    'contact':contact,
                    'category5':category5,
                }
                return render(request,'root/portfolio-details.html',context=context)
            except:
                return render(request,'root/404.html')
    elif request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submitted successfully')
            return redirect(request.path_info)
        else:
            messages.add_message(request,messages.ERROR,'your email invalid')
            return redirect(request.path_info)
                


             
             

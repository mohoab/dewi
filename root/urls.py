from django.urls import path
from django.shortcuts import redirect
from . import views
app_name = 'root'

urlpatterns = [
    path('', views.homepage,name='home'),
    #path('inner', views.inner,name='inner'),
    path('products', views.products,name='products'),
    path('products/<str:cat>', views.products,name='products_cat'),
    path('products/<str:decat>', views.products,name='products_dcat'),
    path('products/<str:bname>', views.products,name='products_brand'),
    path('products/detail/<int:id>',views.details,name='detail'),
    
        
]



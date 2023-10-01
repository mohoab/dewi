from django.urls import path
from . import views
app_name = 'root'
urlpatterns = [
    path('', views.homepage,name='home'),
    #path('inner', views.inner,name='inner'),
    path('products', views.products,name='products'),
    path('products/<str:cat>', views.products,name='products_cat'),
    path('products/<int:decat>', views.products,name='products_dcat'),
]
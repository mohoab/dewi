from django.db import models

class Info(models.Model):
    title = models.CharField(max_length=10)
    years = models.IntegerField(default=1)
    orders = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class About(models.Model):
    title = models.CharField(max_length=199)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']
class Future(models.Model):
    title = models.CharField(max_length=50)
    content= models.CharField(max_length=150)
    img = models.ImageField(upload_to='image/future',default='images/default/default.png')
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
class Question(models.Model):
    que=models.CharField(max_length=50)
    title =models.CharField(max_length=50)
    awnser=models.TextField()
    status = models.BooleanField(default=True )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.que
    class Meta:
        ordering = ['-created_date']
class Service(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(max_length=170)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
class Contact(models.Model):
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    call=models.IntegerField()
    twitter=models.TextField(null=True,blank=True)  
    instagram=models.TextField(null=True,blank=True)  
    linkdin=models.TextField(null=True,blank=True)
    facebook=models.TextField(null=True,blank=True)
    skype=models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Brand(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/brands',default='image/default/default.png')
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_date']

class Category(models.Model):
    title=models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
class Deepcat(models.Model):
    title=models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']



class Product(models.Model):
    title=models.CharField(max_length=75)
    content = models.TextField()
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/product',default='image/default/default.png')
    price = models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    deepcat = models.ForeignKey(Deepcat , on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    counted_view = models.IntegerField(default=0)
    counted_like = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def d_cat(self):
        return self.deepcat.id
    class Meta:
        ordering = ['-created_date']


class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
class Contact_f(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name

    
        

        












































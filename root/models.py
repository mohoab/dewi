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
    img= models.ImageField(upload_to='images/future',default='images/default/default.png')
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
    email2=models.EmailField(null=True)
    call=models.IntegerField()
    call2=models.IntegerField(null=True)
    twitter=models.TextField(null=True)  
    instagram=models.TextField(null=True)  
    linkdin=models.TextField(null=True)
    facebook=models.TextField(null=True)
    skype=models.TextField(null=True)

    def __str__(self):
        return self.title

class Brand(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/brands')
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
    catname=models.ForeignKey(Category , on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
class Image(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='image/portfolio',default='images/default/default.png')
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
class Product(models.Model):
    title=models.CharField(max_length=75)
    content = models.TextField()
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE)
    image = models.ManyToManyField(Image)
    price = models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    deepcat = models.ForeignKey(Deepcat , on_delete=models.CASCADE)
    brand=models.ManyToManyField(Brand)
    counted_view = models.IntegerField(default=0)
    counted_like = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
   











































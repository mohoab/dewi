from django.shortcuts import render

def homepage(request):
    return render(request,'root/index.html')
def inner(request):
    return render(request,'root/inner-page.html')
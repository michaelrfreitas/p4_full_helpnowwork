from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home/home_page.html')


def about_us(request):
    return render(request, 'home/about_us.html')

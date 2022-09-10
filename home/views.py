from django.shortcuts import render, redirect, get_object_or_404
from .models import SupportModel
from .forms import SupportForm


def home(request):
    return render(request, 'home/home_page.html')


def about_us(request):
    return render(request, 'home/about_us.html')


def donate(request):
    return render(request, 'home/donate.html')


def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('loggedcase')
    form = SupportForm()
    context = {
        'form': form
    }
    return render(request, 'home/support.html', context)

def loggedcase(request):
    return render(request, 'home/loggedcase.html')
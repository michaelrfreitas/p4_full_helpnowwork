from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SupportModel
from .forms import SupportForm

def home(request):
    return render(request, 'home/home_page.html')


def about_us(request):
    return render(request, 'home/about_us.html')


def donate(request):
    return render(request, 'home/donate.html')

@login_required(redirect_field_name='account_login')
def contr_portal(request):
    if request.user.profile == 'CONTRIBUTOR':
        return render(request, 'portal/contr_portal.html')
    return render(request, 'portal/error.html')

@login_required(redirect_field_name='account_login')
def admin_portal(request):
    if request.user.profile == 'ADMINISTRATOR':
        return render(request, 'portal/admin_portal.html')
    return render(request, 'portal/error.html')

@login_required(redirect_field_name='account_login')
def user_portal(request):
    if request.user.profile == 'USER':
        return render(request, 'portal/user_portal.html')
    return render(request, 'portal/error.html')

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
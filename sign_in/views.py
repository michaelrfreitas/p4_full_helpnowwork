from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomUser


@login_required(redirect_field_name='account_login')
def edit_users(request):
    if request.user.profile == 'ADMINISTRATOR':
        users = CustomUser.objects.all()
        context = {
            'users': users
        }
        return render(request, 'account/edit_users.html', context)


@login_required(redirect_field_name='account_login')
def delete_user(request, user_id):
    """This is a docstring which describes the module"""
    if request.user.profile == 'ADMINISTRATOR':
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return redirect('edit_users')

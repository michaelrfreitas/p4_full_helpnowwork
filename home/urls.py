from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('donate', views.donate, name='donate'),
    path('support', views.support, name='support'),
    path('loggedcase', views.loggedcase, name='loggedcase'),
    path('contr_portal', views.contr_portal, name='contr_portal'),
    path('admin_portal', views.admin_portal, name='admin_portal'),
    path('user_portal', views.user_portal, name='user_portal'),

]

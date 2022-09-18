from django.urls import path
from . import views

urlpatterns = [
    path('send_question', views.send_question, name='send_question'),
    path('send_answer', views.send_answer, name='send_answer'),
    path('question_list', views.question_list, name='question_list'),
    path('edit/<question_slug>', views.edit_question, name='edi_question'),
    path('delete/<question_slug>', views.delete_question, name='delete_question'),
    path('all_questions', views.all_questions, name='all_questions'),
    path('view_question/<question_slug>', views.view_question, name='view_question')
]
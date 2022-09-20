from django.urls import path
from . import views

urlpatterns = [
    path('send_question', views.send_question, name='send_question'),
    path('send_answer/<question_slug>', views.send_answer, name='send_answer'),
    path('question_list', views.question_list, name='question_list'),
    path('edit/<question_slug>', views.edit_question, name='edi_question'),
    path('delete/<question_slug>', views.delete_question, name='delete_question'),
    path('all_questions', views.all_questions, name='all_questions'),
    path('view_question/<question_slug>', views.view_question, name='view_question'),
    path('answer_list', views.answer_list, name='answer_list'),
    path('edit_answer/<answer_id>', views.edit_answer, name='edit_answer'),
    path('delete_answer/<answer_id>', views.delete_answer, name='delete_answer'),
    path('approved_answer/<answer_id>', views.approved_answer, name='approved_answer'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
]
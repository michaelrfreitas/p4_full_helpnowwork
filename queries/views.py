from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import QuestionModel, AnswerModel
from .forms import QuestionForm, AnswerForm
from django.utils.text import slugify
from django.contrib import messages


@login_required(redirect_field_name='account_login')
def send_question(request):
    if request.user.profile == 'USER':
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                element = form.save(commit=False)
                element.user = request.user
                element.slug = slugify(element.question)
                element.save()
                return redirect('question_list')
            else:
                messages.warning(request, 'This question already exists.')
        form = QuestionForm()
        context = {
            'form': form
        }
        return render(request, 'queries/send_question.html', context)
    return render(request, 'portal/error.html')


@login_required(redirect_field_name='account_login')
def send_answer(request):
    if request.user.profile == 'CONTRIBUTOR':
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                element = form.save(commit=False)
                element.contributor = request.user
                element.save()
                return redirect('answer_list')
        form = AnswerForm()
        context = {
            'form': form
        }
        return render(request, 'queries/send_answer.html', context)
    return render(request, 'portal/error.html')


@login_required(redirect_field_name='account_login')
def question_list(request):
    questions = QuestionModel.objects.filter(user=request.user)
    context = {
        'questions': questions
    }
    return render(request, 'queries/question_list.html', context)


@login_required(redirect_field_name='account_login')
def edit_question(request, question_slug):
    """This is a docstring which describes the module"""
    question = get_object_or_404(QuestionModel, slug=question_slug)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_list')
        else:
            messages.warning(request, 'This question already exists.')
    form = QuestionForm(instance=question)
    context = {
        'form': form
    }
    return render(request, 'queries/edit_question.html', context)


@login_required(redirect_field_name='account_login')
def delete_question(request, question_slug):
    """This is a docstring which describes the module"""
    question = get_object_or_404(QuestionModel, slug=question_slug)
    question.delete()
    return redirect('question_list')


@login_required(redirect_field_name='account_login')
def all_questions(request):
    questions = QuestionModel.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'queries/all_questions.html', context)


@login_required(redirect_field_name='account_login')
def view_question(request, question_slug):
    question = QuestionModel.objects.filter(slug=question_slug)
    context = {
        'question': question
    }
    return render(request, 'queries/view_question.html', context)
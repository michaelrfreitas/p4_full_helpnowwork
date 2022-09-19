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
def send_answer(request, question_slug):
    if request.user.profile == 'CONTRIBUTOR':
        question = get_object_or_404(QuestionModel, slug=question_slug)
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                element = form.save(commit=False)
                element.subject_question = QuestionModel.objects.get(
                    slug=question_slug)
                element.contributor = request.user
                element.save()
                return redirect('all_questions')
        form = AnswerForm()
        context = {
            'form': form,
            'question': question
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
    answer = AnswerModel.objects.filter(subject_question=QuestionModel.objects.get(slug=question_slug), approved=True)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_list')
        else:
            messages.warning(request, 'This question already exists.')
    form = QuestionForm(instance=question)
    context = {
        'form': form,
        'answer': answer
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
    answer = AnswerModel.objects.filter(
        subject_question=QuestionModel.objects.get(slug=question_slug), approved=True)
    context = {
        'question': question,
        'answer': answer
    }
    return render(request, 'queries/view_question.html', context)


@login_required(redirect_field_name='account_login')
def answer_list(request):
    if request.user.profile == 'ADMINISTRATOR':
        answers = AnswerModel.objects.all()
    else:
        answers = AnswerModel.objects.filter(contributor=request.user)
    context = {
        'answers': answers
    }
    return render(request, 'queries/answer_list.html', context)


@login_required(redirect_field_name='account_login')
def edit_answer(request, answer_id):
    """This is a docstring which describes the module"""
    answer = get_object_or_404(AnswerModel, id=answer_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            element = form.save(commit=False)
            element.approved = False
            element.save()
            return redirect('answer_list')
        else:
            messages.warning(request, 'This answer already exists.')
    form = AnswerForm(instance=answer)
    context = {
        'form': form,
        'answer': answer

    }
    return render(request, 'queries/edit_answer.html', context)


@login_required(redirect_field_name='account_login')
def delete_answer(request, answer_id):
    """This is a docstring which describes the module"""
    answer = get_object_or_404(AnswerModel, id=answer_id)
    answer.delete()
    return redirect('answer_list')

@login_required(redirect_field_name='account_login')
def approved_answer(request, answer_id):
    """This is a docstring which describes the module"""
    answer = get_object_or_404(AnswerModel, id=answer_id)
    answer.approved = not answer.approved
    answer.save()
    return redirect('answer_list')
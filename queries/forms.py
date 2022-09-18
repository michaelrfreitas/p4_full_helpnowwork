from django import forms
from .models import QuestionModel, AnswerModel

class QuestionForm (forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = ['question', 'category']

class AnswerForm (forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = ['body']


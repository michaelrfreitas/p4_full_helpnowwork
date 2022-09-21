"""This is a docstring which describes the module"""
from django.test import TestCase
from .forms import QuestionForm, AnswerForm


class TestQuestionForm(TestCase):
    """This is a docstring which describes the module"""
    def test_question_is_required(self):
        """This is a docstring which describes the module"""
        form = QuestionForm({'question': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('question', form.errors.keys())
        self.assertEqual(form.errors['question'][0], 'This field is required.')

    def test_category_is_required(self):
        """This is a docstring which describes the module"""
        form = QuestionForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """This is a docstring which describes the module"""
        form = QuestionForm()
        self.assertEqual(form.Meta.fields, ['question', 'category'])

class TestAnswerForm(TestCase):
    """This is a docstring which describes the module"""
    def test_body_is_required(self):
        """This is a docstring which describes the module"""
        form = AnswerForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """This is a docstring which describes the module"""
        form = AnswerForm()
        self.assertEqual(form.Meta.fields, ['body'])
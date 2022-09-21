"""This is a docstring which describes the module"""
from django.test import TestCase
from .models import QuestionModel, AnswerModel
from sign_in.views import CustomUser


class TestViews(TestCase):
    """This is a docstring which describes the module"""

    def test_send_question_get(self):
        """This is a docstring which describes the module"""
        CustomUser.objects.create_user(email='test@test.com', username='Test', password='Testing2022', profile='USER')
        self.client.login(email='test@test.com', password='Testing2022')
        response = self.client.get('/send_question')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'queries/send_question.html')

    def test_send_question_post(self):
        """This is a docstring which describes the module"""
        CustomUser.objects.create_user(email='test@test.com', username='Test', password='Testing2022', profile='USER')
        self.client.login(email='test@test.com', password='Testing2022')
        response = self.client.post('/send_question', {'question': 'Test Questions?', 'category': 'Others'})
        self.assertRedirects(response, '/question_list')


    def test_send_answer_get(self):
        """This is a docstring which describes the module"""
        CustomUser.objects.create_user(email='test@test.com', username='Test', password='Testing2022', profile='USER')
        self.client.login(email='test@test.com', password='Testing2022')
        response = self.client.post('/send_question', {'question': 'Test Questions?', 'category': 'Others'})
        CustomUser.objects.create_user(email='test2@test.com', username='Test2', password='Testing2022', profile='CONTRIBUTOR')
        self.client.login(email='test2@test.com', password='Testing2022')
        response = self.client.get('/send_answer/test-questions')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'queries/send_answer.html')

    def test_send_answer_post(self):
        """This is a docstring which describes the module"""
        CustomUser.objects.create_user(email='test@test.com', username='Test', password='Testing2022', profile='USER')
        self.client.login(email='test@test.com', password='Testing2022')
        response = self.client.post('/send_question', {'question': 'Test Questions?', 'category': 'Others'})
        CustomUser.objects.create_user(email='test2@test.com', username='Test2', password='Testing2022', profile='CONTRIBUTOR')
        self.client.login(email='test2@test.com', password='Testing2022')
        response = self.client.post('/send_answer/test-questions', {'body': 'Test Answer.'})
        self.assertRedirects(response, '/all_questions')

    def test_get_edit_question(self):
        """This is a docstring which describes the module"""
        # pylint: disable=no-member
        CustomUser.objects.create_user(email='test@test.com', username='Test', password='Testing2022', profile='USER')
        self.client.login(email='test@test.com', password='Testing2022')
        self.client.post('/send_question', {'question': 'Test Questions?', 'category': 'Others'})
        response = self.client.get('/edit/test-questions')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'queries/edit_question.html')

    def test_post_edit_question(self):
        """This is a docstring which describes the module"""
        # pylint: disable=no-member
        CustomUser.objects.create_user(email='test@test.com', username='Test', password='Testing2022', profile='USER')
        self.client.login(email='test@test.com', password='Testing2022')
        question = QuestionModel.objects.create(question='Test Question?', category='Others', user=CustomUser.objects.get(email='test@test.com'))
        response = self.client.post(f'/edit/{question.slug}', {'question': 'Test Question updated?', 'category': 'Critical'})
        self.assertRedirects(response, '/question_list')
        updated_question = QuestionModel.objects.get(slug=question.slug)
        self.assertEqual(updated_question.question, 'Test Question updated?')


    def test_get_edit_answer(self):
        """This is a docstring which describes the module"""
        # pylint: disable=no-member
        CustomUser.objects.create_user(email='test@test.com', username='Test', password='Testing2022', profile='CONTRIBUTOR')
        CustomUser.objects.create_user(email='test2@test.com', username='Test2', password='Testing2022', profile='USER')
        self.client.login(email='test@test.com', password='Testing2022')
        question = QuestionModel.objects.create(question='Test Question?', category='Others', user=CustomUser.objects.get(email='test2@test.com'))
        answer = AnswerModel.objects.create(body='Test Answer', subject_question=QuestionModel.objects.get(id=question.id), contributor=CustomUser.objects.get(email='test@test.com'))
        response = self.client.get(f'/edit_answer/{answer.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'queries/edit_answer.html')
    
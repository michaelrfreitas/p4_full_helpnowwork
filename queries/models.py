from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

CATEGORY = (
    ('Work Permit', 'Work Permit'),
    ('Critical Skill', 'Critical Skill'),
    ('Application Process', 'Application Process'),
    ('Stamp', 'Stamp'),
    ('Sponsorship', 'Sponsorship'),
    ('Qualifications', 'Qualifications'),
    ('Others', 'Others'),
)

class QuestionModel(models.Model):
    question = models.CharField(max_length=300, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY, default='Others')
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.question

class AnswerModel(models.Model):
    subject_question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name='answers')
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contr_users')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Answer {self.body} by {self.contributor}"
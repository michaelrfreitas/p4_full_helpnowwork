from django.db import models

STATUS = ((0, "OPEN"), (1, "PENDING"), (2, "RESOLVED"))

class SupportModel(models.Model):
    subject = models.CharField(max_length=200)
    details = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    email = models.EmailField(max_length=200, unique=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.subject


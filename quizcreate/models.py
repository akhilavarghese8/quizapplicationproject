from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role_options = [
        ('superadmin', 'superadmin'),
        ('user', 'user'),
    ]
    
    role = models.CharField(max_length=200, choices=role_options)

    # def __str__(self):
    #     return self.username


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.IntegerField(choices=((1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')))

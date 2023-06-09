from django.contrib import admin
from quizcreate.models import  Question,QuizResult, User

# Register your models here.
admin.site.register(Question)
admin.site.register(QuizResult)
admin.site.register(User)

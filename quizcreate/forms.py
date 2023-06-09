from django import forms
# from django.contrib.auth.models import User
from quizcreate.models import User
from django.contrib.auth.forms import UserCreationForm
from quizcreate.models import Question, QuizResult

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.TextInput(attrs={"forms":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"forms":"form-control"}))
    
    class Meta:
        model=User
        fields=["username","email","role"]

        widget={
            "username":forms.TextInput(attrs={"forms":"form-control"}),
            "email":forms.EmailInput(attrs={"forms":"form-control"}),
        }

class LoginForm(forms.Form):
    
    username=forms.CharField(widget=forms.TextInput(attrs={"form":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"form":"form-control"}))
    
        
class QuestionForm(forms.ModelForm):

    class Meta:
        model=Question
        fields=["question_text","option_1","option_2","option_3","option_4","answer"]


class QuizResultForm(forms.ModelForm):
    class Meta:
        model=QuizResult
        fields="__all__"
        





        



from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView,View,FormView,ListView,UpdateView,TemplateView
from quizcreate.forms import RegistrationForm,LoginForm,QuestionForm,QuizResultForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from quizcreate.models import Question,QuizResult
from quizcreate.models import User,AbstractUser





def superadminsignin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.role == 'superadmin':
            return fn(request,*args,**kwargs)
        else:
            return redirect('error')
    return wrapper



def usersignin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.role  == 'user':
            return fn(request,*args,**kwargs)
        else:
            return redirect('error')    

    return wrapper

class SignUpView(CreateView):
    model=User
    template_name='register.html'
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")



def logoutview(request,*args,**kwargs):
    logout(request)
    return redirect('signin')




class SignInView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            usrn=form.cleaned_data.get("username")
            passw=form.cleaned_data.get("password")
            user=authenticate(request,username=usrn,password=passw)
            if user:
                login(request, user)
                print(user)
                if request.user.role == 'superadmin':
                    return redirect('super-index')
                elif request.user.role == 'user':
                    return redirect('user-index')

                
                
                
            else:
                
                messages.error(request, 'Invalid username and passwod, Please try again.')
                return render(request,"login.html",{"form":form})

        return render(request,"login.html",{"form":form})
            
class ErrorPageView(TemplateView):
    template_name='errorpage.html'

 
class IndexView(CreateView):
    model=Question
    form_class=QuestionForm
    template_name="index.html"
    success_url=reverse_lazy("user-index")
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class SuperAdminIndexView(ListView):
    model=Question
    template_name="superbase.html"
    context_object_name='listquestions'


 


class QuestionListView(ListView):
    model=Question
    template_name='question_list.html'
    context_object_name='questions'



    # def get_queryset(self):
    #     return Question.objects.filter(is_active=True)


class QuestionAddView(CreateView):
    model=Question
    form_class=QuestionForm
    template_name='question_add.html'
    success_url=reverse_lazy('super-index')
    

    def form_valid(self,form):
       form.instance.user=self.request.user
       return super().form_valid(form)
    
class QuestionUpdateView(UpdateView):
    model=Question
    form_class=QuestionForm
    template_name="question_update.html"
    
    success_url=reverse_lazy("listquestions")    


    # def form_valid(self, form):
    #     qn=Question.objects.get(user=self.request.user)
    #     form.instance.company=qn
    #     return super().form_valid(form)
class QuestionDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Question.objects.get(id=id).delete()     
        return redirect('super-index') 
    
# class   QuestionDeleteView(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get('id')
#         question=Question.objects.filter(id=id)
#         Question.objects.filter(id=id).update(is_active=False)
#         return redirect('super-index')


class QuizResultView(View):
    def get(self, request,*args,**kwargs):
        # Display a form to input quiz answers
        questions = Question.objects.all()
        score=0
        for q in questions:
            if q.answer == request.GET.get(q.question_text):
                
                score+=1
                print(request.GET)
        return render(request,'result.html',{'score':score})
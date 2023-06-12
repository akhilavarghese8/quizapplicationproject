from django.urls import path
from quizcreate import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("userhome/",views.IndexView.as_view(),name="user-index"),
    # path("superindex/",views.QuestionView.as_view(),name="listquestions"),
    path("superadminhome/",views.SuperAdminIndexView.as_view(),name="super-index"),
    path('questions/',views.QuestionListView.as_view(), name='question_list'),
    path('questions/<int:pk>/update/',views.QuestionUpdateView.as_view(),name='question_update'),
    path('questions/<int:id>/delete/',views.QuestionDeleteView.as_view(),name='question-delete'),
    path('questions/add/',views.QuestionAddView.as_view(),name='question_add'),
    path('questionlist/',views.QuestionAddView.as_view(),name="listquestions"),
    path('answers/',views.QuestionListView.as_view(),name="answer-add"),
    path('results/', views.QuizResultView.as_view(), name='results'),
    path("logout/",views.logoutview,name="logout"),
    path('error/',views.ErrorPageView.as_view(),name='error'),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

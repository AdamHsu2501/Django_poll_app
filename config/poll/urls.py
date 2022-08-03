from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import UserLoginView, UserRegisterView, QusetionListView, QuestionDetailView, submit, QuestionResultView



urlpatterns = [
    path('login/', view=UserLoginView.as_view(), name="login" ),
    path('logout/', view=LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', view=UserRegisterView.as_view(), name="register"),

    path('', view=QusetionListView.as_view(), name="question-list"),
    path('question/<int:pk>/', view=QuestionDetailView.as_view(), name="question"),
    path('question/<int:question_id>/submit/', view=submit, name='submit'),
    path('question/<int:pk>/result/', view=QuestionResultView.as_view(), name="result")
]

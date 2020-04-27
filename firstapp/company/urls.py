from django.urls import path
from . import views



urlpatterns = [
    #path("", views.MoviesView.as_view()),
    # path("training/answer/", views.QuestionsTrainingList.as_view(), name="answer"),
    path("", views.MainCompanyList.as_view(), name="main_company"),
    # path('company/detail/', views.ResultScore.as_view(), name='result'),
    path("create/", views.MainCompanyControl.as_view(), name="company_control"),
    #path("answers/<int:pk>/", views.GetAnswersForQuestion.as_view(), name="answers"),
]

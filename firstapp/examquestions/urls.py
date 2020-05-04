from django.urls import path
from . import views



urlpatterns = [
    #path("", views.MoviesView.as_view()),
    # path("training/answer/", views.QuestionsTrainingList.as_view(), name="answer"),
    path("training/<str:pk>/", views.QuestionsTrainingList.as_view(), name="training"),
<<<<<<< HEAD
    path('examing/result/', views.ResultScore.as_view(), name='result'),
    path("examing/<str:pk>/", views.QuestionsExamingList.as_view(), name="examing"),
=======
>>>>>>> 9ae2595edc73348e4848f3ec4d26be7368b7c1c3
    #path("answers/<int:pk>/", views.GetAnswersForQuestion.as_view(), name="answers"),
]

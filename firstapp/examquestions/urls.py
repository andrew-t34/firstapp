from django.urls import path
from . import views



urlpatterns = [
    #path("", views.MoviesView.as_view()),
    # path("training/answer/", views.QuestionsTrainingList.as_view(), name="answer"),
    path("training/<str:pk>/", views.QuestionsTrainingList.as_view(), name="training"),
    #path("answers/<int:pk>/", views.GetAnswersForQuestion.as_view(), name="answers"),
]

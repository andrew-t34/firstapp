from django.urls import path
from . import views



urlpatterns = [
    #path("", views.MoviesView.as_view()),
    path("training/<int:pk>/", views.QuestionsTrainingList.as_view(), name="training"),
    path("answers/<int:pk>/", views.GetAnswersForQuestion.as_view(), name="answers"),
]

from django.urls import path
from . import views


urlpatterns = [
    #path("", views.MoviesView.as_view()),
    path("<int:id>/", views.TopicDetailView.as_view(), name="stadytopic"),
    path("program/", views.GetMyProgramms.as_view(), name="stadyprogram"),
]

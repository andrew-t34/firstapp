from django.urls import path
from . import views


urlpatterns = [
    #path("", views.MoviesView.as_view()),
    path("<int:id>/", views.TopicDetailView.as_view(), name="stadytopic"),
    #path('about/', TemplateView.as_view(template_name="about.html")),
    path("program/", views.GetMyProgramms.as_view(), name="stadyprogram"),
    path("program/list/<int:pk>/", views.StadyProgramList.as_view(), name="stadyprogramlist"),
]

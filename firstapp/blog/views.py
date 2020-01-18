from django.shortcuts import render
from django.views.generic.base import View
from .models import StadyTopic, StadyProgram
from django.contrib.auth.models import User
# Create your views here.

class TopicDetailView(View):
    def get(self, request, id):
        stadytopic = StadyTopic.objects.get(id=id)
        #stadytopic = "НОвое название заголовка"
        #print(id)
        print(request.user.id)
        return render(request, 'blog/stadytopic.html', {"stadytopic": stadytopic})

class GetMyProgramms(View):
    def get(self, request):
        stadyprogram = StadyProgram.objects.all()
        return render(request, 'blog/program.html', {"stadyprogram": stadyprogram})

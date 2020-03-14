from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionGroupMixin
from django.views.generic.base import View
from .models import StadyTopic, StadyProgram, StadyModul
from django.contrib.auth.models import User
# Create your views here.
from django.utils.decorators import method_decorator


class TopicDetailView(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']

    def get(self, request, id):
        stadytopic = StadyTopic.objects.get(id=id)
        #stadytopic = "НОвое название заголовка"
        #print(id)
        #print(request.user.id)
        return render(request, 'blog/stadytopic.html', {"stadytopic": stadytopic})


class GetMyProgramms(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']
    def get(self, request):
        stadyprogram = StadyProgram.objects.all()
        return render(request, 'blog/program.html', {"stadyprogram": stadyprogram})

class StadyProgramList(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']
    id_user_programm = 1 #Временно указвваем id программы по которйй пользователь будет обучатся.

    def get(self, request, pk):
        stadymoduls = StadyModul.objects.all().filter(stadyprogram_id = pk).order_by('ordermodul')
        stadytopics = StadyTopic.objects.all().filter(stadyprogram_id = pk).order_by('ordertopic')

        return render(request, 'blog/programlist.html', {"stadymoduls": stadymoduls, "stadytopics": stadytopics})

        #return render(request, 'не определено', {"?": ?})

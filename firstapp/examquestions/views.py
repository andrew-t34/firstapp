import random
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import PermissionGroupMixin
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Question, Answer
# Create your views here.
from django.utils.decorators import method_decorator
# from examquestions.forms import AnswerForm

# Create your views here.

class QuestionsTrainingList(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']

    def get(self, request, pk):

        questions = Question.objects.all().filter(stadyprogram_id = pk)#рандомная выборка через

        if 'questions' not in request.session:
            questions = random.sample(list(questions), 3)
            number = 1
            listquestions = {}
            for question in questions:
                listquestions.setdefault(str(number), dict(id = question.id, textques =  question.text, check = 'none'))
                number += 1
            request.session['questions'] = listquestions
            questions = listquestions
            pk = '1'
        else:
            questions = request.session['questions']
        pk = str(pk)
        answers = self.getanswers(questions[pk]['id'])
        return render(request, 'examquestions/training.html', {"questions": questions, "answers": answers, "numquest": pk})

    def getanswers(self, pk):
        answers = Answer.objects.all().filter(question_id = pk)
        return answers

    def post(self, request, pk):
        number = str(pk)
        session = request.session['questions'][number]
        answers = Answer.objects.all().filter(id = request.POST[number])
        session.update({'check': answers[0].check})
        #print(request.session['questions'])
        #print(request.POST[pk])
        pk += 1
        return HttpResponseRedirect(reverse('training', args=str(pk)))

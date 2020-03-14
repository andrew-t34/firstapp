import random
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionGroupMixin
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Question, Answer
# Create your views here.
from django.utils.decorators import method_decorator

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
                listquestions.setdefault(number, question.id)
                number += 1
            request.session['questions'] = listquestions
            questions = listquestions
        else:
            questions = request.session['questions']
        return render(request, 'examquestions/training.html', {"questions": questions})


class GetAnswersForQuestion(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']

    def get(self, request, pk):
        answers = Answer.objects.all().filter(question_id = pk)
        return render(request, 'examquestions/training.html', {"questions": request.session['questions'], "answers": answers })

    def post(self, request):
        pass

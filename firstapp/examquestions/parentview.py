import random
from django.contrib.auth.mixins import PermissionGroupMixin
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Question, Answer



class ParentTestList(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']


    def getQuestionsByIdProgramm(self, request, id, max_questions):
        if 'questions' not in request.session:
            #В этом варианте id это id программы прграммы обучения.
            questions = Question.objects.all().filter(stadyprogram_id = id)
            questions = random.sample(list(questions), max_questions)
            listquestions = {}
            for n, question in enumerate(questions):
                listquestions.setdefault(str(n+1), dict(id = question.id, textques =  question.text, check = 'none'))
            request.session['questions'] = listquestions
            questions = listquestions
            self.num_question = 1
        else:
            #В этом варианте id это порядковый номер вопроса записанный в сессию
            self.num_question = id
            questions = request.session['questions']
        return questions


    def getanswers(self, pk):
        answers = Answer.objects.all().filter(question_id = pk)
        return answers

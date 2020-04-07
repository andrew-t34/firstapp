import random
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.mixins import PermissionGroupMixin
from django.urls import reverse
# from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Question, Answer
from .parentview import ParentTestList
# Create your views here.
from django.utils.decorators import method_decorator
from examquestions.forms import AnswerForm, TestForm

# Create your views here.

class QuestionsTrainingList(ParentTestList):
    def __init__(self):
        self.max_questions = 3
        self.num_question = '1'
        self.user_answer = 'none'

    def get(self, request, pk):
        #при превом запросе страницы - ()методом  get) pk это id программы обучения. Далее (метод post) pk это номер вопроса.Подробнее в parenview.py
        questions = self.getQuestionsByIdProgramm(request, pk, self.max_questions)
        print(request.session['questions'])
        # print(self.num_question)
        answers = self.getanswers(questions[self.num_question]['id'])
        if 'user_answers' in request.session:
            if str(pk) in request.session['user_answers']:
                self.user_answer = request.session['user_answers'][str(pk)]
        form = AnswerForm(answers = answers, user_answer = self.user_answer)
        return render(request, 'examquestions/training.html', {"form": form,"questions": questions, "answers": answers, "numquest": self.num_question, "user_answer": self.user_answer})

        #ВИМАНИЕ.. После POST запроса делается редирект по методу GET поэтому не будет видно
    def post(self, request, pk):
        self.num_question = pk
        # session = request.session['questions'][self.num_question]
        answers = Answer.objects.all().filter(id = request.POST['user_answer'])
        request.session['questions'][self.num_question].update({'check': answers[0].check})
        if 'user_answers' not in request.session:
            request.session['user_answers'] = {}
        request.session['user_answers'].setdefault(self.num_question, answers[0].id)
        pk += 1
        return HttpResponseRedirect(reverse('training', args=pk))


class QuestionsExamList(ParentTestList):
    pass

import random
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from permission.views import PermissionGroupMixin
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Question, Answer
from .parentview import ParentTestList
from django.http import Http404
# Create your views here.
from django.utils.decorators import method_decorator


# Create your views here.

class QuestionsTrainingList(ParentTestList):
    def __init__(self):
        super().__init__()
        self.MAX_QUESTIONS = 4

    def get(self, request, pk):
        #при превом запросе страницы - ()методом  get) pk это id программы обучения. Далее (метод post) pk это номер вопроса.Подробнее в parenview.py
        super().get(request, pk)
        return render(request, 'examquestions/training.html', {"form": self.form, "questions": self.questions, "answers": self.answers, "numquest": self.num_question})

        #ВИМАНИЕ.. После POST запроса делается редирект по методу GET поэтому не будет видно
    def post(self, request, pk):
        if int(pk) == self.MAX_QUESTIONS:
            return HttpResponseRedirect(reverse('training', args='1'))
        else:
            super().post(request, pk)
            next_question = int(pk) + 1
            return HttpResponseRedirect(reverse('training', args=str(next_question)))

# ВНИМАНИЕ НУЖЕН ДЕКОРАТОР ДЛЯ ПРОВЕРКИ ТИПА ТЕСТИРОВАНИЯ ТРЕНИРОВКА ИЛИ ЭКЗАМЕН.
# С ЭКЗАМЕНА МОЖНО ПОПАСТЬ В ТРЕНИРОВКУ ПРИ ВВЕДЕНИИ АДРЕСНОЙ СТРОКИ.
class QuestionsExamingList(ParentTestList):
    def __init__(self):
        super().__init__()
        self.MAX_QUESTIONS = 4

    def get(self, request, pk):
        super().get(request, pk)
        return render(request,'examquestions/examing.html', {"form": self.form, "questions": self.questions, "answers": self.answers, "numquest": self.num_question})

    def post(self, request, pk):
        super().post(request, pk)
        if len(request.session['user_answers']) == self.MAX_QUESTIONS:
            return HttpResponseRedirect(reverse('result'))
        elif int(pk) == self.MAX_QUESTIONS:
            return HttpResponseRedirect(reverse('examing', args='1'))
        else:
            next_question = int(pk) + 1
            return HttpResponseRedirect(reverse('examing', args=str(next_question)))
            # return redirect()

# class ParentResultScore(PermissionGroupMixin, View): в parentview  c целью наследования
class ResultScore(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']

    def get(self, request):
        list = QuestionsExamingList()
        user_answers = request.session['user_answers']
        questions =request.session['questions']
        count_correct_answer = 0
        for k, v in request.session['questions'].items():
            count_correct_answer += v['check']

        count_correct_answer = (count_correct_answer * 100)/list.MAX_QUESTIONS
        if 'questions' in request.session:
            del request.session['questions']
        if 'user_answers' in request.session:
            del request.session['user_answers']
            # if int(a['check']) == 0:
            #     count_correct_answer += 1
        return render(request, 'examquestions/resultpage.html', {"data": questions, 'count_correct_answer': count_correct_answer})


    def general_calculation(self, data):
        pass

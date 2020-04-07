import random
from permission.views import PermissionGroupMixin
from django.urls import reverse
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Question, Answer
from examquestions.forms import AnswerForm



class ParentTestList(PermissionGroupMixin, View):
    permission_required = ['listener', 'admin']
    # permission_required = ['listener']
    def __init__(self):
        # self.num_question задали как строковое значение для выбора вопроса № по умолчанию в сессии.
        self.num_question = '1'
        self.questions = '' # dict
        self.answers = '' # list
        # self.user_answer = '' # string
        self.form = '' # object
        self.user_answer = 'none' # string


    def get(self, request, pk):
        # print(dir(dict))
        #при превом запросе страницы - ()методом  get) pk это id программы обучения. Далее (метод post) pk это номер вопроса.Подробнее в parenview.py
        self.getQuestionsByIdProgramm(request, pk, self.MAX_QUESTIONS)
        self.getAnswersByIdQuestion(self.questions[self.num_question]['id'])
        self.form = AnswerForm(answers = self.answers, user_answer = self.get_user_answer(request, pk))

    def post(self, request, pk):
        #pk - это номер текущего вопроса после отправки формы str
        self.user_answer = Answer.objects.all().filter(id = request.POST['user_answer'])
        request.session['questions'][pk].update({'check': self.user_answer[0].check})
        # Проверяем есть ли в сессии словарь с ключем user_answers. Если нет создаем.
        self.set_user_answer(request, pk, self.user_answer)

    def getQuestionsByIdProgramm(self, request, id, max_questions):
        if 'questions' not in request.session:
            #В этом варианте id это id программы прграммы обучения.
            questions = Question.objects.all().filter(stadyprogram_id = id)
            questions = random.sample(list(questions), max_questions)
            listquestions = {}
            # Записываем при момощи итерации данные в сессию.
            for n, question in enumerate(questions):
                listquestions.setdefault(str(n+1), dict(id = question.id, textques =  question.text, check = 'none'))
            request.session['questions'] = listquestions
            request.session['user_answers'] = {}
            self.questions = listquestions
            # self.num_question = str(1)
        else:
            #В этом варианте id это порядковый номер вопроса записанный в сессию
            self.num_question = id
            self.questions = request.session['questions']
        # return questions

    def getAnswersByIdQuestion(self, pk):
        self.answers = Answer.objects.all().filter(question_id = pk)

    def get_user_answer(self, request, pk: str):
        if pk in request.session['user_answers']:
            return request.session['user_answers'][pk]
        return 'none'

    def set_user_answer(self, request, pk: str, user_answer):
        request.session['user_answers'].setdefault(pk, user_answer[0].id)

class ParentResultScore(PermissionGroupMixin, View):
    pass

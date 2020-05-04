from django import forms
from django.forms import widgets


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # Варианты ответов из базы данных по id вопроса.. см. views.py метод get
        answers = kwargs.pop ('answers')
        # Записанный в сессию ответ слушателя
        user_answer = kwargs.pop ('user_answer')
        super(AnswerForm, self).__init__(*args, **kwargs)
        CHOICES = []
        # формируем СПИСОК вопросов для виджета forms.RadioSelect
        for answer in answers:
            a = (str(answer.id), answer.text)
            CHOICES.append(a)
        self.fields['user_answer'] = forms.ChoiceField(
            widget = forms.RadioSelect,
            choices = CHOICES,
            label = '',
            help_text = 'Выбрать один ответ',
            error_messages = {'required': 'Please enter your name'},
            required = True,
            initial = user_answer)


<<<<<<< HEAD
# class TestForm(forms.Form):
#     CHOICES = [('1', 'First'), ('2', 'Second')]
#     #print(type(CHOICES[1]))
#     # CHOICES = {'11': 'Вообще ни каких.. Херней занимается всегда.', '12': 'Работает как лошадь... И жнец и на трубе дудец', '13': 'Смотрите статью ТК РФ... Сам не знаю'}
#     choice_field = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES)
=======
class TestForm(forms.Form):
    CHOICES = [('1', 'First'), ('2', 'Second')]
    #print(type(CHOICES[1]))
    # CHOICES = {'11': 'Вообще ни каких.. Херней занимается всегда.', '12': 'Работает как лошадь... И жнец и на трубе дудец', '13': 'Смотрите статью ТК РФ... Сам не знаю'}
    choice_field = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES)
>>>>>>> 9ae2595edc73348e4848f3ec4d26be7368b7c1c3

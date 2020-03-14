from django.db import models
from blog.models import StadyModul, StadyProgram, StadyTopic

# Create your models here.
class Question(models.Model):
    #Градация уровня обучения
    stadyprogram = models.ForeignKey(StadyProgram, null = True, on_delete=models.SET_NULL, verbose_name="Программа обучения")
    stadymodul = models.ForeignKey(StadyModul, null = True, on_delete=models.SET_NULL, verbose_name="Модуль обучения")
    stadytopic = models.ForeignKey(StadyTopic, null = True, on_delete=models.SET_NULL, verbose_name="Тема обучения")
    text = models.TextField(verbose_name="Текст вопроса")

    class Meta:
        verbose_name_plural = "Воросы к тесту"

    def __str__(self):
        return (self.text)

class Answer(models.Model):
    #Градация уровня обучения
    question = models.ForeignKey(Question, null = True, on_delete=models.SET_NULL, verbose_name="Ответы к вопросам")
    text = models.TextField(verbose_name="Текст ответа")
    check = models.IntegerField(verbose_name="Правильный ответ")

    class Meta:
        verbose_name_plural = "Оветы к вопросам"

    def __str__(self):
        return (self.text)

#class Trainings(models.Model)
    #user = models.ForeignKey(User)
    ##programm = #здесь внешинй на программу
    #questions = models.ManyToMany(Qustions) #связь с вопросами. Список примари кей.

from django.contrib import admin

from examquestions.models import Question, Answer
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("stadyprogram", "text")
    list_filter = ("stadyprogram",)

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "text")
    list_filter = ("question",)

admin.site.register(Answer, AnswerAdmin)

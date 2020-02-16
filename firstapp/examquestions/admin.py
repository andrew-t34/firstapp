from django.contrib import admin

from examquestions.models import Question, Answer
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)

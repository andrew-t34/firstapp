from django.contrib import admin

from blog.models import StadyLevel, StadyModul, StadyProgram, StadyTopic, StadyField
# Register your models here.
admin.site.register(StadyLevel)
admin.site.register(StadyModul)
admin.site.register(StadyProgram)
admin.site.register(StadyTopic)
admin.site.register(StadyField)

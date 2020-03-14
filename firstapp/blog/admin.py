from django.contrib import admin
from django import forms
from blog.models import StadyLevel, StadyModul, StadyProgram, StadyTopic, StadyField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class StadyTopicAdminForm(forms.ModelForm):

    text = forms.CharField(label = 'Содержание', widget=CKEditorUploadingWidget())

    class Meta:
        model = StadyTopic
        fields = '__all__'
# Register your models here.
admin.site.register(StadyLevel)
admin.site.register(StadyModul)
admin.site.register(StadyProgram)



class StadyTopicAdmin(admin.ModelAdmin):
    list_display = ("stadyprogram", "title", "release_date")
    list_filter = ("stadyprogram",)
    form = StadyTopicAdminForm
    # fields = ("title",)

    class Media:
         js = ("js/blog/admin_topic_select.js",)

admin.site.register(StadyTopic, StadyTopicAdmin)
admin.site.register(StadyField)

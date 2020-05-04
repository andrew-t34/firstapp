from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
# from django.core.files.uploadedfile import SimpleUploadedFile
import re
# from django.core.exceptions import ValidationError
from .models import Type, Company, Division, Worker

def clean_telephon(value):
    match = re.fullmatch(r'(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})', value)
    if not match:
        raise forms.ValidationError("Формат номера должен быть 8(111)222-33-44")
    return value

def clean_ogrn(value):
    match = re.fullmatch(r'(\d{15})', value)
    if not match:
        raise forms.ValidationError("Вы должны ввести число из 15 цифр")
    return value


def clean_inn(value):
    match = re.fullmatch(r'(\d{10})', value)
    if not match:
        raise forms.ValidationError("Вы должны ввести число из 10 цифр")
    return value

def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Файл слишком большой. размер должен быть не более 2 MiB.')

class CompanyForm(forms.Form):


    # id = forms.IntegerField(widget=forms.HiddenInput(), label='')
    id = forms.IntegerField(label='id', initial = 0, widget = forms.HiddenInput() )


    type_id = forms.ModelChoiceField(
        queryset = Type.objects.all(),
        to_field_name = "id",
        empty_label = "Пусто",
        label = "Форма собственности",
        required = True,
        widget = forms.Select(
            attrs = {
                'class': 'form-control'
            }))

    name = forms.CharField(
        max_length=100,
        label="Название компани",
        error_messages={'required': 'Поле обязательное для заполнеия'},
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Рога и копыта',
                'class': 'form-control'
            }))

    ogrn = forms.CharField(
        max_length=15,
        label="ОГРН",
        required = True,
        help_text = 'Число из 15 знаков',
        validators=[clean_ogrn],
        widget = forms.TextInput(
            attrs = {
                'placeholder': '773452345674',
                'class': 'form-control'
            }))

    inn = forms.CharField(
        max_length=10,
        label="ИНН",
        validators=[clean_inn],
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': '773452345674',
                'class': 'form-control'
            }))

    telephon = forms.CharField(
        max_length=50,
        label="Номер телефона",
        validators=[clean_telephon],
        required = True,
        help_text = 'Телефон компании',
        widget = forms.TextInput(
            attrs = {
                'placeholder': '+79160146441',
                'class': 'form-control'
            }))

    logo = forms.ImageField(
        label="Логотип компании",
        required = False,
        validators=[file_size],)

    url = forms.CharField(
        label="Адрес сайта",
        help_text = 'Корпоративный сайт компании',
        validators=[validators.URLValidator()],
        initial = 'http://',
        widget = forms.URLInput(
            attrs = {
                'class': 'form-control',
            }))

    text = forms.CharField(
        label="Дополнительная информация",
        required = False,
        validators=[validators.MaxLengthValidator(500)],
        widget=forms.Textarea(
            attrs = {
                'placeholder': 'Допускается объем текста не более 500 символов',
                'class': 'form-control',
                'rows':3,
            }))

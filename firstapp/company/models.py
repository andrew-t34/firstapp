from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# Create your models here.

fs = FileSystemStorage(location='/media/company/logo')

class Type(models.Model):
    #Градация уровня обучения
    name_short = models.CharField(max_length=30, verbose_name="Программа обучения")
    name_long = models.CharField(max_length=100, verbose_name="Программа обучения")


    class Meta:
        verbose_name_plural = "Форма собственности"

    def __str__(self):
        return (self.name_long)

class Company(models.Model):
    #Градация уровня обучения
    type = models.ForeignKey(Type, models.SET_NULL, blank=True, null=True, verbose_name="Форма собственности")
    user = models.ForeignKey(User, models.SET_NULL, db_index = True, related_name='type_id',  blank=True, null=True, verbose_name="Пользователь")
    name = models.CharField(max_length=100, verbose_name="Название компани")
    ogrn = models.CharField(max_length=15, verbose_name="ОГРН")
    inn = models.CharField(max_length=12, verbose_name="ИНН")
    telephon = models.CharField(max_length=50, default = '', verbose_name="Номер телефона")
    url = models.URLField(max_length=50, verbose_name="Сайт компании")
    date_create = models.DateField(auto_now_add = True, verbose_name="Дата создания")
    date_updata = models.DateField(auto_now = True, verbose_name="Дата изменения")
    logo = models.ImageField('Логотип компании', storage=fs, upload_to = 'company/logo/', null=True, blank = True)
    text = models.TextField(verbose_name="Текст вопроса")
    activated = models.IntegerField(default = 0, verbose_name="Активация")

    class Meta:
        verbose_name_plural = "Данные компании"

    def __str__(self):
        return (self.full_name_company)

    @property
    def full_name_company(self):
        "Returns the person's full name."
        return '%s %s' % (self.type, self.name)


class Division(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания")
    name = models.CharField(max_length=100, verbose_name="Имя")
    parent =  models.ForeignKey('self', models.SET_NULL, blank=True, null=True, related_name='+')

    class Meta:
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return (self.full_name)

class Worker(models.Model):
    company = models.ForeignKey(Company, models.SET_NULL, blank=True, null=True, related_name='+', verbose_name="Компания")
    division = models.ForeignKey(Division,  models.SET_NULL, blank=True, null=True, verbose_name="Компания")
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name =  models.CharField(max_length=15, verbose_name="Фамилия")
    patronymic_name = models.CharField(max_length=30, verbose_name="Отчество")
    job_position = models.CharField(max_length=100, verbose_name="Должность/Профессия")
    snils = models.CharField(max_length = 20, verbose_name="СНИЛС")
    employment_day = models.DateField(verbose_name="Дата приема")
    doc_study = models.FileField('Документ об образовании',upload_to = 'company/doc_study/', default = '', blank = True)

    class Meta:
        verbose_name_plural = "Работники"

    def __str__(self):
        return (self.full_name_worker)

    @property
    def full_name_worker(self):
        "Returns the person's full name."
        return '%s %s %s' % (self.last_name, self.first_name, self.patronymic_name)

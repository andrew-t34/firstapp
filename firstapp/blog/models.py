from django.db import models

# Create your models here.
class StadyLevel(models.Model):
    #Градация уровня обучения
    name = models.CharField(max_length=30, verbose_name="Уровень обучения",)

    class Meta:
        verbose_name_plural = "Уровени обучения"

    def __str__(self):
        return (self.name)


class StadyField(models.Model):
    #Градация области обучения
    stadylevel = models.ForeignKey(StadyLevel, null = True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30, verbose_name="Область обучения",)

    class Meta:
        verbose_name_plural = "Области обучения"

    def __str__(self):
        return (self.name)


class StadyProgram(models.Model):
    #Градация программ обучения
    stadyfield = models.ForeignKey(StadyField, null = True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30, verbose_name="Программа обучения")
    fullname = models.TextField(default='', verbose_name="Полное название")

    class Meta:
        verbose_name_plural = "Программы обучения"

    def __str__(self):
        return (self.name)

class StadyModul(models.Model):
    #Градация программ обучения
    stadyprogram = models.ForeignKey(StadyProgram, null = True, on_delete=models.SET_NULL)
    ordermodul =  models.IntegerField(default=0, verbose_name="Порядковый номер")
    name = models.CharField(max_length=255, verbose_name="Модуль обучения")

    class Meta:
        verbose_name_plural = "Модули обучения"

    def __str__(self):
        return (self.name)

    def get_topic(self):
        return self.stadytopic_set.all()


class StadyTopic(models.Model):
    #Градация области обучения
    stadyfield = models.ForeignKey(StadyField, null = True, on_delete=models.SET_NULL, verbose_name="Область обучения")
    stadyprogram = models.ForeignKey(StadyProgram, null = True, on_delete=models.SET_NULL, verbose_name="Программа обучения")
    stadymodul = models.ForeignKey(StadyModul, null = True, on_delete=models.SET_NULL, verbose_name="Модуль обучения")
    ordertopic =  models.IntegerField(default=0, verbose_name="Порядковый номер")
    title = models.CharField(max_length=30, verbose_name="Заголовок",)
    picture = models.ImageField('Картинка',upload_to = 'blog/picture/', default = '', blank = True)
    text = models.TextField(verbose_name="Содержание")
    release_date = models.DateField(verbose_name="Дата создания")
    update_date = models.DateField(verbose_name="Дата обновления")
    num_stars = models.IntegerField(verbose_name="Рейтинг")

    class Meta:
        verbose_name_plural = "Темы обучения"

    def __str__(self):
        return (self.title)

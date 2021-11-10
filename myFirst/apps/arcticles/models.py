import datetime
from django.db import models
from django.utils import timezone


class Arcticle(models.Model):
    title = models.CharField('Мақала атауы', max_length=200)
    text = models.TextField('Мақала тексті')
    pub_date = models.DateTimeField('Уақыт')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    arcticle = models.ForeignKey(Arcticle, on_delete=models.CASCADE)
    name = models.CharField('Автор есімі', max_length=50)
    text = models.CharField('Коммент',  max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
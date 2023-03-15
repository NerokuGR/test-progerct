from django.db import models


class Task(models.Model):
    title = models.CharField('Задача', max_length=23)
    task = models.TextField('Описание')

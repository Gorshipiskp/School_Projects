import library_cypher as cyp
from django.db import models


class Answers(models.Model):
    name = models.CharField('Название теста', max_length=50)
    subject = models.CharField('Предмет', max_length=20)
    krypto = models.CharField('Криптоключ', max_length=300)
    variants = models.IntegerField('Количество вариантов')
    date = models.CharField('Дата', max_length=105)
    author = models.CharField('Создатель', max_length=500)
    contains = models.TextField('Содержание (ответы, вопросы...)', max_length=8500)
    is_checked = models.BooleanField('Одобрен ли ответ?')

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

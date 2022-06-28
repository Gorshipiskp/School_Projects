from django.db import models


class Answers(models.Model):
    name = models.CharField('Название товара', max_length=75)
    desc = models.TextField('Описание товара')
    price = models.IntegerField('Цена товара')
    weight = models.IntegerField('Вес товара (граммы)')
    category = models.CharField('Категория товара', max_length=95)
    price_weight = models.BooleanField('Цена за вес?')
    available = models.BooleanField('Товар в наличии?')
    image = models.TextField('Ссылка на изображение')

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

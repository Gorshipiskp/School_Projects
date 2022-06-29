# Generated by Django 4.0.2 on 2022-06-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otveti', '0005_alter_answers_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='is_checked',
            field=models.BooleanField(default=True, verbose_name='Одобрен ли ответ?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answers',
            name='contains',
            field=models.TextField(max_length=8500, verbose_name='Содержание (ответы, вопросы...)'),
        ),
    ]
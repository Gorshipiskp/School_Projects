# Generated by Django 4.0.2 on 2022-06-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otveti', '0003_alter_answers_author_alter_answers_krypto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='date',
            field=models.CharField(max_length=105, verbose_name='Дата'),
        ),
    ]

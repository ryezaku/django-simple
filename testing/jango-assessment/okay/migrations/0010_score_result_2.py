# Generated by Django 4.1.2 on 2022-10-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okay', '0009_remove_score_result_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='result_2',
            field=models.IntegerField(default=100, verbose_name='result_2'),
        ),
    ]
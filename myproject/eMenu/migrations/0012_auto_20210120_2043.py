# Generated by Django 3.0.7 on 2021-01-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0011_auto_20210120_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data dodania menu'),
        ),
        migrations.AlterField(
            model_name='card',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Data zmiany menu'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='add_time',
            field=models.DateTimeField(default='2021-01-20 19:43:58', verbose_name='Data dodania przep.'),
        ),
    ]

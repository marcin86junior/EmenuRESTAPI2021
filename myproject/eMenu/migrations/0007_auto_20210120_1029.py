# Generated by Django 3.0.7 on 2021-01-20 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eMenu', '0006_auto_20210120_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nazwa menu')),
                ('description', models.CharField(max_length=500, verbose_name='Opis menu')),
                ('add_time', models.DateTimeField(default='2021-01-20 09:29:17', verbose_name='Data dodania menu')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data zmiany menu')),
            ],
            options={
                'verbose_name': 'karta menu',
                'verbose_name_plural': 'karty menu',
                'ordering': ('name',),
                'managed': True,
            },
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='dish_wege',
            new_name='wege',
        ),
        migrations.AlterField(
            model_name='dish',
            name='add_time',
            field=models.DateTimeField(default='2021-01-20 09:29:17', verbose_name='Data dodania przep.'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nazwa dania'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-13 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210313_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giveaway',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='participant',
            name='joined',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
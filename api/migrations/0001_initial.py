# Generated by Django 3.1.7 on 2021-03-13 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Giveaway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
                ('prize', models.CharField(max_length=256)),
                ('winners', models.PositiveIntegerField()),
                ('eligibility', models.TextField()),
                ('rules', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('giveaway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', related_query_name='giveaways', to='api.giveaway')),
            ],
            options={
                'unique_together': {('username', 'giveaway')},
            },
        ),
    ]
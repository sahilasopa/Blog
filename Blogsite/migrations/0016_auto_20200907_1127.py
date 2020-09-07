# Generated by Django 3.1 on 2020-09-07 05:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blogsite', '0015_auto_20200907_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloguser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
    ]

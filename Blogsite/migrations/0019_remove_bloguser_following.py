# Generated by Django 3.1 on 2020-09-07 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogsite', '0018_auto_20200907_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='following',
        ),
    ]
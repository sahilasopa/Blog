# Generated by Django 3.1 on 2020-08-16 12:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogsite', '0011_auto_20200816_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

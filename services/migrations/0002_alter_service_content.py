# Generated by Django 4.1.7 on 2024-01-08 03:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='contenido'),
        ),
    ]

# Generated by Django 4.2.16 on 2024-12-03 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0010_remove_choicesolution_marks_descsolution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='partial_marking',
        ),
    ]
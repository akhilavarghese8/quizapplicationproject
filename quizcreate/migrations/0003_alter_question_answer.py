# Generated by Django 4.2.1 on 2023-06-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizcreate', '0002_remove_question_correct_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200),
        ),
    ]
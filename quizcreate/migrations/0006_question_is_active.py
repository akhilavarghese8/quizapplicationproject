# Generated by Django 4.2.2 on 2023-06-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizcreate', '0005_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-05 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210805_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='a_question',
            new_name='question',
        ),
    ]

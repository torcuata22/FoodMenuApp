# Generated by Django 4.1.2 on 2022-10-28 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user_name',
        ),
    ]

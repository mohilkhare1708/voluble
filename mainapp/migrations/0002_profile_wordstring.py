# Generated by Django 3.1.12 on 2021-10-11 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wordString',
            field=models.CharField(default='', max_length=4000),
        ),
    ]
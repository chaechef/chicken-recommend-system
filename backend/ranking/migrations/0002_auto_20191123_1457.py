# Generated by Django 2.2.7 on 2019-11-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='itemname',
        ),
        migrations.AddField(
            model_name='ranking',
            name='chickenID',
            field=models.IntegerField(default=0),
        ),
    ]
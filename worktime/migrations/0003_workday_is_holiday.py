# Generated by Django 2.2 on 2019-05-11 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0002_auto_20190509_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='workday',
            name='is_holiday',
            field=models.BooleanField(default=False),
        ),
    ]

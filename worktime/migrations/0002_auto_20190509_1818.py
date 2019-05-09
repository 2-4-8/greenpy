# Generated by Django 2.2 on 2019-05-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worktime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='additional_issues_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workday',
            name='come_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='workday',
            name='issues_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='workday',
            name='leave_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='workday',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
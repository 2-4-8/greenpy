# Generated by Django 2.2 on 2019-05-09 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=1)),
                ('year', models.PositiveSmallIntegerField()),
                ('comment', models.TextField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='months', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_work_day', models.PositiveSmallIntegerField(null=True)),
                ('date', models.DateField()),
                ('come_time', models.TimeField()),
                ('leave_time', models.TimeField()),
                ('issues_completed', models.IntegerField()),
                ('additional_issues_completed', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('comment', models.TextField(null=True)),
                ('work_month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='worktime.WorkMonth')),
            ],
        ),
    ]

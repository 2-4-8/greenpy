import datetime
import calendar
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


MONTH_CHOICES = (
    (i, calendar.month_name[i])
    for i in range(1, 13)
)


class WorkMonth(models.Model):
    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES, default=1)
    year = models.PositiveSmallIntegerField()
    owner = models.ForeignKey('auth.User', related_name='months', on_delete=models.CASCADE)
    comment = models.TextField(null=True)


@receiver(post_save, sender=WorkMonth)
def post_save(sender, instance, **kwargs):
    if instance.days.count() == 0:
        for day in range(calendar.monthrange(instance.year, instance.month)[1]):
            current_work_day = 0
            date = datetime.date(instance.year, instance.month, day+1)
            if date.weekday() in range(0,5):
                current_work_day += 1
                work_day = WorkDay(date=date, work_month=instance, num_of_work_day=current_work_day)
            else:
                work_day = WorkDay(date=date, work_month=instance)
            work_day.save()
            instance.days.add(work_day)


class WorkDay(models.Model):
    num_of_work_day = models.PositiveSmallIntegerField(null=True)
    date = models.DateField()
    come_time = models.TimeField(null=True)
    leave_time = models.TimeField(null=True)
    issues_completed = models.IntegerField(default=0)
    additional_issues_completed = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    work_month = models.ForeignKey('WorkMonth', related_name='days', on_delete=models.CASCADE)
    comment = models.TextField(null=True)

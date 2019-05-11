import datetime
import calendar
import statistics
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
    owner = models.ForeignKey('auth.User', related_name='periods', on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    def get_days_count(self):
        return self.days.count()

    def get_work_days_count(self):
        return self.days.exclude(num_of_work_day__isnull=True).count()

    def get_average_come_time(self):
        days = self.days.exclude(num_of_work_day__isnull=True).exclude(come_time__isnull=True)
        times = list(map(lambda x: x.come_time, days))
        times_in_seconds = list(map(lambda x: ((x.hour * 60) + x.minute) * 60 + x.second, times))
        average_time = statistics.mean(times_in_seconds)
        return (datetime.datetime.min + datetime.timedelta(seconds=average_time)).time()

    def get_average_leave_time(self):
        days = self.days.exclude(num_of_work_day__isnull=True).exclude(leave_time__isnull=True)
        times = list(map(lambda x: x.leave_time, days))
        times_in_seconds = list(map(lambda x: ((x.hour * 60) + x.minute) * 60 + x.second, times))
        average_time = statistics.mean(times_in_seconds)
        return (datetime.datetime.min + datetime.timedelta(seconds=average_time)).time()

    def get_average_issues_completed(self):
        days = self.days.exclude(num_of_work_day__isnull=True)
        issues = list(map(lambda x: x.issues_completed, days))
        return statistics.mean(issues)

    def get_average_additional_issues(self):
        days = self.days.exclude(num_of_work_day__isnull=True)
        issues = list(map(lambda x: x.additional_issues_completed, days))
        return statistics.mean(issues)

    def get_average_salary(self):
        days = self.days.exclude(num_of_work_day__isnull=True)
        salaries = list(map(lambda x: x.salary, days))
        return statistics.mean(salaries)

    def get_average_work_time(self):
        days = self.days.exclude(num_of_work_day__isnull=True)
        times = list(map(lambda x: x.get_work_time(), days))
        return statistics.mean(times)

    def get_sum_issues_completed(self):
        days = self.days.all()
        issues = list(map(lambda x: x.issues_completed, days))
        return sum(issues)

    def get_sum_additional_issues(self):
        days = self.days.all()
        issues = list(map(lambda x: x.additional_issues_completed, days))
        return sum(issues)

    def get_sum_salary(self):
        days = self.days.all()
        salaries = list(map(lambda x: x.salary, days))
        return sum(salaries)

    def get_sum_work_time(self):
        days = self.days.all()
        work_time_list = list(map(lambda x: x.get_work_time(), days))
        return sum(work_time_list)


@receiver(post_save, sender=WorkMonth)
def post_save(sender, instance, **kwargs):
    if instance.days.count() == 0:
        for day in range(calendar.monthrange(instance.year, instance.month)[1]):
            current_work_day = 0
            date = datetime.date(instance.year, instance.month, day + 1)
            if date.weekday() in range(0, 5):
                current_work_day += 1
                work_day = WorkDay(date=date, work_month=instance, num_of_work_day=current_work_day)
            else:
                work_day = WorkDay(date=date, work_month=instance)
            work_day.save()
            instance.days.add(work_day)


class WorkDay(models.Model):
    num_of_work_day = models.PositiveSmallIntegerField(null=True)
    is_holiday = models.BooleanField(default=False)
    date = models.DateField()
    come_time = models.TimeField(null=True)
    leave_time = models.TimeField(null=True)
    issues_completed = models.IntegerField(default=0)
    additional_issues_completed = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    work_month = models.ForeignKey('WorkMonth', related_name='days', on_delete=models.CASCADE)
    comment = models.TextField(null=True)

    def get_work_time(self):
        if self.come_time and self.leave_time:
            return (
                datetime.datetime.combine(self.date, self.leave_time)
                - datetime.datetime.combine(self.date, self.come_time)
            ).seconds
        else:
            return 0

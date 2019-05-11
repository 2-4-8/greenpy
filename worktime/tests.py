import datetime
from django.test import TestCase
from django.contrib.auth.models import User

from worktime.models import WorkMonth, WorkDay


class WorkTimeModelsTest(TestCase):
    def setUp(self):
        self.test_user = User()
        self.test_user.save()

    def tearDown(self):
        self.test_user.delete()
        self.test_user = None

    def test_new_month_have_days(self):
        january = WorkMonth(month=1, year=2019, owner=self.test_user)
        january.save()
        days_count = january.days.count()
        right_days_count = 31
        january.delete()
        self.assertEqual(days_count, right_days_count)

    def test_day_work_time(self):
        month = WorkMonth(month=1, year=2019, owner=self.test_user)
        month.save()
        day: WorkDay = month.days.first()
        day.come_time = datetime.time(9, 0, 0)
        day.leave_time = datetime.time(18, 30, 0)
        day.save()
        time_diff = day.get_work_time()
        right_time_diff = ((18 - 9) * 60 + 30) * 60
        month.delete()
        self.assertEqual(time_diff, right_time_diff)

    # TODO: Test this later
    # def test_month_methods(self):
    #     # 2, 3 days of march 2019 is holidays
    #     month = WorkMonth(month=3, year=2019, owner=self.test_user)
    #     month.save()
    #     first_five_days = mont

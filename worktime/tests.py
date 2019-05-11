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

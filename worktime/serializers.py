from rest_framework import serializers
from django.contrib.auth.models import User
from worktime.models import WorkMonth, WorkDay


class WorkMonthCreationSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    days = serializers.HyperlinkedRelatedField(many=True, view_name='workday-detail', read_only=True)
    days_count = serializers.IntegerField(source='get_days_count', read_only=True)

    class Meta:
        model = WorkMonth
        fields = ('url', 'month', 'year', 'comment', 'days', 'owner', 'days_count')


class WorkMonthRetrieveSerializer(WorkMonthCreationSerializer):
    class Meta:
        model = WorkMonth
        fields = ('url', 'month', 'year', 'comment', 'days', 'owner', 'days_count')
        read_only_fields = ('month', 'year')


class WorkDaySerializer(serializers.HyperlinkedModelSerializer):
    work_time = serializers.IntegerField(source='get_work_time', read_only=True)

    class Meta:
        model = WorkDay
        fields = (
            'url', 'num_of_work_day', 'is_holiday', 'date', 'come_time', 'leave_time', 'issues_completed',
            'additional_issues_completed', 'salary', 'work_month', 'comment', 'work_time'
        )
        read_only_fields = ('num_of_work_day', 'date', 'work_month')

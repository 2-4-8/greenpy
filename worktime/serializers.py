from rest_framework import serializers
from django.contrib.auth.models import User
from worktime.models import WorkMonth, WorkDay

TIME_FORMAT = '%H:%M'


class WorkDaySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    come_time = serializers.TimeField(format=TIME_FORMAT, input_formats=[TIME_FORMAT,])
    leave_time = serializers.TimeField(format=TIME_FORMAT, input_formats=[TIME_FORMAT,])
    work_time = serializers.IntegerField(source='get_work_time', read_only=True)

    class Meta:
        model = WorkDay
        fields = '__all__'
        read_only_fields = ('num_of_work_day', 'date', 'work_month')


class WorkMonthCreationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    days = WorkDaySerializer(many=True, read_only=True)
    days_count = serializers.IntegerField(source='get_days_count', read_only=True)
    work_days_count = serializers.IntegerField(source='get_work_days_count', read_only=True)
    average_come_time = serializers.TimeField(source='get_average_come_time', read_only=True, format=TIME_FORMAT)
    average_leave_time = serializers.TimeField(source='get_average_leave_time', read_only=True, format=TIME_FORMAT)
    average_issues_completed = serializers.DecimalField(None, 2, source='get_average_issues_completed', read_only=True)
    average_additional_issues = serializers.DecimalField(None, 2, source='get_average_additional_issues', read_only=True)
    average_salary = serializers.DecimalField(None, 2, source='get_average_salary', read_only=True)
    average_work_time = serializers.IntegerField(source='get_average_work_time', read_only=True)
    sum_issues_completed = serializers.IntegerField(source='get_sum_issues_completed', read_only=True)
    sum_additional_issues = serializers.IntegerField(source='get_sum_additional_issues', read_only=True)
    sum_salary = serializers.IntegerField(source='get_sum_salary', read_only=True)
    sum_work_time = serializers.IntegerField(source='get_sum_work_time', read_only=True)

    class Meta:
        model = WorkMonth
        fields = '__all__'


class WorkMonthRetrieveSerializer(WorkMonthCreationSerializer):
    class Meta:
        model = WorkMonth
        fields = '__all__'
        read_only_fields = ('month', 'year')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    periods = serializers.HyperlinkedRelatedField(many=True, view_name='workmonth-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'periods')

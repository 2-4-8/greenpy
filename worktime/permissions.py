from rest_framework import permissions


class IsOwnerOrReject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        if obj.work_month.owner:
            return obj.work_month.owner == request.user
        return False

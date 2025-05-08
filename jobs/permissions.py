from rest_framework import permissions

class IsEmployer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'employer'

class IsJobOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.employer == request.user
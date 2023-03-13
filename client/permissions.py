from rest_framework import permissions


class IsAdminOrReadonly(permissions.BasePermission):
    """
    Пермишн дает воспользоваться безопасными методами всем,
    не безопасные методы только администратор
    """
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пермишн дает права редактирования только авторам.
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user
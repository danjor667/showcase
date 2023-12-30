from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permision to handle the delete and update od a model
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
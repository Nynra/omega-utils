from rest_framework import permissions


class ApiReadOnly(permissions.BasePermission):

    def _has_permission(self, request, view):
        """This method checks if the request is a read only request."""
        return request.method in permissions.SAFE_METHODS
    
    def has_permission(self, request, view):
        """This method checks if the request is a read only request."""
        return self._has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        """This method checks if the request is a read only request."""
        return self._has_permission(request, view)
        

class ApiWriteOnly(permissions.BasePermission):

    def _has_permission(self, request, view):
        """This method checks if the request is a write only request."""
        return request.method not in permissions.SAFE_METHODS
    
    def has_permission(self, request, view):
        """This method checks if the request is a write only request."""
        return self._has_permission(request, view)
    
    def has_object_permission(self, request, view, obj):
        """This method checks if the request is a write only request."""
        return self._has_permission(request, view)
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Allows access only to superuser workers.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

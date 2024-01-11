from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
      if request.user.permission.name in 'Admin':
          return True
      return False

class FinanceManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
      if request.user.permission.name in ['Admin', 'FinanceManager']:
          return True
      return False

class ManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
      if request.user.permission.name in ['Admin', 'Manager']:
        return True
      return False

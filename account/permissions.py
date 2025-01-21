from rest_framework import permissions
from . models import CustomUser,MemberProfile
from gym.models import Booking

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'staff'
    
class IsAuthororReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.member == request.user

class IsMember(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.member == request.user
    
class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
        
        
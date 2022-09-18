from rest_framework import permissions

class IsAdmin(permissions.BasePermission) :
    """
    just admin permission
    """

    message = 'you dont have admin privileges'

    def has_permission(self, request, view):
        
        if request.user.is_authenticated :
            return request.user.is_admin

        return False

class IsOwner(permissions.BasePermission) :
   """
   each user has permission for editting its own resume
   """ 
   def has_object_permission(self, request, view, obj):

        if obj.user_profile.user == request.user:
            return True

        return False

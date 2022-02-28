from math import perm
from rest_framework import permissions

## if a user is admin can do anything or if a non user read only
## inherit the base permission

'''
has object -> a particular permission
Example: the individual review can be edited by it's woner
'''

# Checks if the user is admin for request except get
class AdminOrReadOnly(permissions.BasePermission):
    
    ## return true or false
    def has_permission(self, request, view):
        ## if the user is admin return true
        admin_permission =  bool(request.user and request.user.is_staff)
        return request.method =="GET" or admin_permission


'''
    safe methods and unsafe methods
    use has object permission cause accessing individual object
'''

class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user
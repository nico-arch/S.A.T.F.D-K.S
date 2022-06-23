from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect


def check_permisions(perm):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if  request.user.has_perm(perm):
                return view_func(request, *args, **kwargs)
            else:
                return render(request, "dashboard/403.html")
        return wrap
    return decorator

def custom_login_required():
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            #if the user is authenticated and is staff = True
            if  request.user.is_staff == False:
                # return render(request, "dashboard/inactive_account.html")
                return redirect('dashboard-login')

            if  request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('dashboard-login')

        return wrap
    return decorator

# def role_required(allowed_roles=[]):
#     def decorator(view_func):
#         def wrap(request, *args, **kwargs):
#             if request.user.profile.userStatus in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return render(request, "dashboard/404.html")
#         return wrap
#     return decorator
#
#
# def admin_only(view_func):
#     def wrap(request, *args, **kwargs):
#         if request.user.profile.userStatus == "admin":
#             return view_func(request, *args, **kwargs)
#         else:
#             return render(request, "dashboard/404.html")
#     return wrap

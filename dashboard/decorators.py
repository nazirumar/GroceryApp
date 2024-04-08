from django.http import HttpResponseRedirect

def user_dashboard_permissions(viewfunc):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated or request.user.is_superuser:
            return viewfunc(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    
    return wrapper_function
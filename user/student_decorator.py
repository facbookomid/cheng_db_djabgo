from django.core.exceptions import PermissionDenieddef superuser_only(func):    def wrapper(request, *args, **kwargs):        if not request.user.is_superuser:            raise PermissionDenied        return func(request, *args, **kwargs)    return wrapperdef myView(request):    pass
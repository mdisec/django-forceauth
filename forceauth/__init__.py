from django.conf.global_settings import LOGIN_URL
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


def publicly_accessible_endpoint(view_func):
    return view_func


class PubliclyAccessibleEndpointMixin:
    publicly_accessible_endpoint = None


class ForceAuthenticationMiddleware(MiddlewareMixin):
    """
    Bla bla bla
    """
    def process_view(self, request, view_func, view_args, view_kwargs):
        # If it's authenticated user we don't have to do anything.
        if request.user.is_authenticated:
            return None
        # We need to decide that view is function or class. Easiest way to do it check existince
        # of view_class attribute of view_func. While __global__ exist on every object,
        # Class-based-views only have view_class.
        if hasattr(view_func, 'view_class'):
            if not hasattr(view_func.view_class, 'publicly_accessible_endpoint'): return HttpResponseRedirect(LOGIN_URL)
        else:
            if 'publicly_accessible_endpoint' not in view_func.__globals__: return HttpResponseRedirect(LOGIN_URL)
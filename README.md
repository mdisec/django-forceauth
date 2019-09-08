# django-forceauth
A Django package that force authentication requirement by default on every single endpoint. 

## Why 'Secure by Design' ?
https://pentest.blog/why-secure-design-matters-secure-approach-to-session-validation-on-modern-frameworks-django-solution/

## Usage
First and foremost, you need to add `forceauth.ForceAuthenticationMiddleware` middleware right after `AuthenticationMiddleware`. This is important.

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'forceauth.ForceAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Usage of `publicly_accessible_endpoint` decorator for function based views.

```
from forceauth import publicly_accessible_endpoint

@publicly_accessible_endpoint
def home(request):
    ...
    return render(request, 'home.html', context={})

```

Usage of `PubliclyAccessibleEndpointMixin` mixin for class based views. 

```
from forceauth import PubliclyAccessibleEndpointMixin
from django.contrib.auth.views import LoginView

class AuthLoginView(LoginView, PubliclyAccessibleEndpointMixin):
    pass
```

For example, let's say that you are using `LoginView` CBV for your authentication mechanism. But `ForceAuthenticationMiddleware` middlware will redirect user back to login because `LoginView` does not have `PubliclyAccessibleEndpointMixin`. So you just need to inherit LoginView and call mixin :)

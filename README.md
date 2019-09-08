# django-forceauth
A Django package that force authentication requirement by default on every single endpoint. 

## Why 'Secure by Design' ?
People are tend to make mistakes. Mistakes made by people lead to software bugs. Software bugs lead to vulnerabilities. For that reason, you must design your software arthictecture in way to prevent other developers to make mistakes. In that context, expecting every single developer to call 'login_required' or 'LoginRequiredMixin' for every single 'view' is a wrong.

So lets force authentication by default. So that people have to call `publicly_accessible_endpoint` or `PubliclyAccessibleEndpointMixin` provided by that package when they want to have endpoint without authentication.



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
from questions.models import Question, Category

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

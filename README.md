# django-authbydefault
A Django package that force authentication requirement by default on every single endpoint. 

## Why 'Secure by Design' ?
People are tend to make mistakes. Mistakes made by people lead to software bugs. Software bugs lead to vulnerabilities. For that reason, you must design your software arthictecture in way to prevent other developers to make mistakes. In that context, expecting every single developer to call 'login_required' or 'LoginRequiredMixin' for every single 'view' is a wrong.

So lets force authentication by default. So that people have to call `publicly_accessible_endpoint` or `PubliclyAccessibleEndpointMixin` provided by that package when they want to have endpoint without authentication.




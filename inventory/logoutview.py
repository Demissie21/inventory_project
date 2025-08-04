from django.contrib.auth.views import LogoutView

class LogoutViewAllowGet(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# In urls.py
path('logout/', LogoutViewAllowGet.as_view(), name='logout'),

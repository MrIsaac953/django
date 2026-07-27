from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            username = user.username
        except User.DoesNotExist:
            pass

        return super().authenticate(
            request,
            username=username,
            password=password,
            **kwargs
        )
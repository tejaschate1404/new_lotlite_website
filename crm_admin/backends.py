from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import UserNew

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserNew.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserNew.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserNew.objects.get(pk=user_id)
        except UserNew.DoesNotExist:
            return None

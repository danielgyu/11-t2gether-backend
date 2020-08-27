import jwt
import json
import requests

from django.http import JsonResponse

from .models import User
import my_setting

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        received_token = request.headers.get('Authorization', None)
        decrypted_token = jwt.decode(received_token, my_setting.SECRET_KEY, algorithm=my_setting.HASH_ALGORITHM)
        user = User.objects.get(id = decrypted_token['user_id'])
        request.user = user

        return func(self, request, *args, **kwargs)
    return wrapper

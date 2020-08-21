import json
import bcrypt
import jwt
import re

from django.views import View
from django.http  import JsonResponse

from .models import User
import my_setting

def pw_validate(pw):
    if len(pw) < 8:
        return False
    is_largeCase = re.compile('[A-Z]')
    is_numeric = re.compile('[0-9]')
    if not(is_largeCase.search(pw)) or not(is_numeric.search(pw)):
        return False
    return True

class JoinView(View):
    def post(self, request):
        try:
            data        = json.loads(request.body)
            input_first = data['first_name']
            input_last  = data['last_name']
            input_email = data['email']
            input_pw    = data['password']
            input_phone = data['phone']
            input_birth = data['birthdate']
            input_news  = data['is_newsletter_subscribed']

            if ('@' not in input_email) or ('.' not in input_email):
                return JsonResponse({'message' : 'WRONG_EMAIL_FORMAT'}, status = 400)
            if not(pw_validate(input_pw)):
                return JsonResponse({'message' : 'WRONG_PASSWORD_CONDITION'}, status = 400)
            if User.objects.filter(email = input_email).exists():
                return JsonResponse({'message' : 'ALREADY_USE_EMAIL'}, status = 400)
            if User.objects.filter(phone = input_phone).exists():
                return JsonResponse({'message' : 'ALREADY_USE_PHONE_NUMBER'}, status = 400)

            User(
                first_name               = input_first,
                last_name                = input_last,
                email                    = input_email,
                phone                    = input_phone,
                password                 = (bcrypt.hashpw(input_pw.encode(my_setting.ENCODING_FORMAT), bcrypt.gensalt())).decode(my_setting.ENCODING_FORMAT),
                birthdate                = input_birth,
                is_newsletter_subscribed = input_news,
                is_top_contributor       = False
            ).save()
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        return JsonResponse({'message' : 'SUCCESS'}, status = 200)

class LogInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            input_email = data['email']
            input_pw    = data['password']

            if not(User.objects.filter(email = input_email).exists()):
                return JsonResponse({'message' : 'WRONG_LOGIN_INFORMATION'}, status = 400)

            saved_password = User.objects.get(email = input_email).password
            if bcrypt.checkpw(input_pw.encode(my_setting.ENCODING_FORMAT), saved_password.encode(my_setting.ENCODING_FORMAT)):
                login_token = jwt.encode({'user_id' : User.objects.get(password = saved_password).id}, my_setting.SECRET_KEY, algorithm = my_setting.HASH_ALGORITHM)
                return JsonResponse({'message' : login_token.decode(my_setting.ENCODING_FORMAT)}, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        return JsonResponse({'message' : 'WRONG_LOGIN_INFORMATION'}, status = 400)

import json
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse

from .models import User
import my_setting

def pw_validate(pw):
    large_case = False
    number     = False
    if len(pw) < 8:
        return False
    for each_item in pw:
        if each_item.isupper():
            large_case = True
        if each_item.isdigit():
            number = True
    if large_case and number:
        return True
    return False

class JoinView(View):
    def post(self, request):
        try:
            data        = json.loads(request.body)
            input_first = data['first_name']
            input_last  = data['last_name']
            input_email = data['email']
            input_pw    = data['password']
            input_phone = data['phone']
            input_birth = data['birth']
            input_news  = data['newsletter']

            if ('@' not in input_email) or ('.' not in input_email):
               return JsonResponse({'message' : 'EMAIL_VALIDATION_FAILED'}, status = 400)
            if pw_validate(input_pw) == False:
                return JsonResponse({'message' : 'PASSWORD_CHECK_FAILED'}, status = 400)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        User(
            first_name      = input_first,
            last_name       = input_last,
            email           = input_email,
            phone           = input_phone,
            password        = (bcrypt.hashpw(input_pw.encode('utf-8'), bcrypt.gensalt())).decode('utf-8'),
            birth           = input_birth,
            newsletter      = input_news,
            top_contributor = False
        ).save()
        return JsonResponse({'message' : 'SUCCESS'}, status = 200)

    def get(self, request):
        return JsonResponse({'message' : 'HTTP GET'}, status = 200)

class LogInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            input_email = data['email']
            input_pw    = data['password']
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        saved_password = User.objects.get(email = input_email).password
        if bcrypt.checkpw(input_pw.encode('utf-8'), saved_password.encode('utf-8')):
            login_token = jwt.encode({'user_id' : User.objects.get(password = saved_password).id}, my_setting.SECRET_KEY, algorithm = 'HS256')
            return JsonResponse({'message' : login_token.decode('utf-8')}, status = 200)
        return JsonResponse({'message' : 'LOGIN_FAILED'}, status = 400)

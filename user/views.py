import json
import bcrypt
import jwt
import re

from django.views import View
from django.http  import JsonResponse

from .models import User, Wishlist, ShoppingBag
from product.models import Product, Size
from .utils import login_decorator
import my_setting

def pw_validate(pw):
    regex_pw = re.compile('^(?=.*[a-z])(?=.*\d)(?=.*[A-Z])[a-z\dA-Z]{8,}$')
    return regex_pw.search(pw)

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

            is_email_format = re.compile('[@]((\.)|(([\w-]+\.)+))')
            if not(is_email_format.search(input_email)):
                return JsonResponse({'message' : 'WRONG_EMAIL_FORMAT'}, status = 400)
            if not(pw_validate(input_pw)):
                return JsonResponse({'message' : 'WRONG_PASSWORD_CONDITION'}, status = 400)
            if User.objects.filter(email = input_email).exists():
                return JsonResponse({'message' : 'ALREADY_USED_EMAIL'}, status = 400)
            if User.objects.filter(phone = input_phone).exists():
                return JsonResponse({'message' : 'ALREADY_USED_PHONE_NUMBER'}, status = 400)

            User(
                first_name = input_first,
                last_name  = input_last,
                email      = input_email,
                phone      = input_phone,
                password   = (bcrypt.hashpw(input_pw.encode(my_setting.ENCODING_FORMAT), bcrypt.gensalt())).decode(my_setting.ENCODING_FORMAT),
                birthdate  = input_birth,
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

            login_user = User.objects.get(email = input_email)
            saved_password = login_user.password
            if bcrypt.checkpw(input_pw.encode(my_setting.ENCODING_FORMAT), saved_password.encode(my_setting.ENCODING_FORMAT)):
                target_id = login_user.id
                login_token = jwt.encode({'user_id' : target_id}, my_setting.SECRET_KEY, algorithm = my_setting.HASH_ALGORITHM)

                login_response = {}
                login_response['access_token'] = login_token.decode(my_setting.ENCODING_FORMAT)
                login_response['first_name'] = login_user.first_name

                response_wish_list = []
                if Wishlist.objects.filter(user_id = login_user).exists():
                    wish_list = Wishlist.objects.filter(user_id = login_user).select_related('product_id')
                    for each_item in wish_list:
                        response_wish_list.append(each_item.product_id.id)
                login_response['user_wish_list'] = response_wish_list

                user_shoppingbag_count = 0
                if ShoppingBag.objects.filter(user_id = login_user).exists():
                    shoppingbag_products = ShoppingBag.objects.filter(user_id = login_user).select_related('product_id')
                    for each_item in shoppingbag_products:
                        user_shoppingbag_count += each_item.count
                login_response['user_shoppingbag_count'] = user_shoppingbag_count
                return JsonResponse({'login response' : login_response}, status = 200)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        return JsonResponse({'message' : 'WRONG_LOGIN_INFORMATION'}, status = 400)

class WishlistView(View):
    @login_decorator
    def post(self, request):
        try:
            data             = json.loads(request.body)
            user             = request.user
            input_product_id = data['product_id']
            if not(Product.objects.filter(id = input_product_id).exists()):
                return JsonResponse({'message':'WRONG_PRODUCT_ID'}, status = 400)

            target_product_id = Product.objects.get(id = input_product_id)
            res_dict = {}
            if Wishlist.objects.filter(user_id = user, product_id = target_product_id).exists():
                Wishlist.objects.filter(user_id = user, product_id = target_product_id).delete()
                res_dict['product_id'] = input_product_id
                res_dict['is_wished'] = False
                return JsonResponse({'message':res_dict}, status = 204)

            Wishlist(
                user_id = user,
                product_id=target_product_id
            ).save()
            res_dict['product_id'] = input_product_id
            res_dict['is_wished']  = True
            return JsonResponse({'message':res_dict}, status = 201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400)

    @login_decorator
    def get(self, request):
        user = request.user
        wish_products = Wishlist.objects.filter(user_id=user).select_related('product_id')
        user_wish_list = [{
            'product_id'    : product.product_id.id,
            'product_name'  : product.product_id.main_name,
            'product_price' : product.product_id.main_price,
            'product_image' : product.product_id.main_image,
            'size_unit'     : [tea.unit for tea in product.product_id.size_set.all()],
            'size_price'    : [tea.price for tea in product.product_id.size_set.all()],
            'size_image'    : [tea.image for tea in product.product_id.size_set.all()],
        } for product in wish_products]
        return JsonResponse({'product_list' : user_wish_list}, status = 200)

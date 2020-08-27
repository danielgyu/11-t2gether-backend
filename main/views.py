import json

from django.views import View
from django.http import JsonResponse

from .models import MainImage

class BodyResourceView(View):
    def get(self, request):
        res_dict = {}

        top_image = MainImage.objects.filter(purpose='Top Image').get()
        res_dict['Top Image'] = top_image.info

        featured = []
        for i in range(5):
            temp = MainImage.objects.filter(purpose='Featured', numbering=i+1).get()
            featured.append(temp.info)
        res_dict['Featured'] = featured

        shop_the_look = MainImage.objects.filter(purpose='Shop THe Look').get()
        res_dict['Shop The Look'] = shop_the_look.info

        partnerships = []
        for i in range(2):
            temp = MainImage.objects.filter(purpose='Partnerships', numbering=i+1).get()
            partnerships.append(temp.info)
        res_dict['Partnerships'] = partnerships

        tea_library = []
        for i in range(6):
            temp = MainImage.objects.filter(purpose='Tea Library', numbering=i+1).get()
            tea_library.append(temp.info)
        res_dict['Tea Library'] = tea_library

        teawares = MainImage.objects.filter(purpose='Teawares').get()
        res_dict['Teawares'] = teawares.info

        brewing_tool = MainImage.objects.filter(purpose='Brewing Tools').get()
        res_dict['Brewing Tools'] = brewing_tool.info

        find_yout_gift = []
        for i in range(4):
            temp = MainImage.objects.filter(purpose='Find Your Gift', numbering=i+1).get()
            find_yout_gift.append(temp.info)
        res_dict['Find Your Gift'] = find_yout_gift

        return JsonResponse({'Main Page Resources':res_dict}, status = 200)

class FooterResourceView(View):
    def get(self, request):
        res_dict = {}

        moving_logo = MainImage.objects.filter(purpose='Moving Logo').get()
        res_dict['Moving Logo'] = moving_logo.info

        footer_bg_image = MainImage.objects.filter(purpose='Footer Background Image').get()
        res_dict['Footer Background Image'] = footer_bg_image.info

        for i in range(6):
            temp_sns_info = MainImage.objects.filter(purpose='SNS', numbering=i+1).get().info[1:-1]
            temp_res = temp_sns_info.split(', ')
            key = 'SNS No.{}'.format(i+1)

            temp_sns_dict = {}
            temp_sns_dict['SNS'] = temp_res[0][1:-1]
            temp_sns_dict['HREF']= temp_res[1][1:-1]
            temp_sns_dict['viewBox'] = temp_res[2][1:-1]
            temp_sns_dict['d'] = temp_res[3][1:-1]
            res_dict[key] = temp_sns_dict

        return JsonResponse({'Footer Resources':res_dict}, status= 200)

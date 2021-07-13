from django.http import HttpResponse
from django.shortcuts import render
import random
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.views import APIView

from verifications.models import SmsSendlog
from yxm.utils.exceptions import logger
from .constants import sms_code_redis_expires,send_sms_code_interval
from yxm.libs.smschinese.sms import SMSC
from yxm.libs.captcha.captcha import captcha


class ImageCodeView(APIView):
    '''图片验证码'''
    def get(self,requset,image_code_id):
        print(image_code_id)
        text,image=captcha.generate_captcha()
        return HttpResponse(image,content_type="jpg")

class SMSCodeView(APIView):
    #自定义限流
    throttle_Scoped ='contacts'
    def get(self,request,mobile):
        #1.生成短信
        sms_code='%06d' % random.randint(0,999999)
        #2.把验证码保存到redis
        redis_conn=get_redis_connection('verify_codes')
        pl=redis_conn.pipeline()
        pl.setex("sms_{}".format(mobile),sms_code_redis_expires,sms_code)
        pl.setex("send_flag_{}".format(mobile),send_sms_code_interval,1)
        pl.execute()
        #3.发送记录进行保存yx
        try:

            SmsSendlog.objects.create(mobile=mobile,code=sms_code)

        except:
            logger.error("{}发送失败".format(mobile))
            return Response({"message":'no'},status=400)
        #sms_code='{:0>2d}' .format(random.randint(0,999999))
        #4.发送短信验证

        #正常方法
        #SMSC(mobile,sms_code)

        #异步发送
        from celery_tasks.sms import tasks as sms_tasks
        sms_tasks.send_sms_code.delay(mobile,sms_code)
        print(mobile, sms_code)

        return Response({"message":'ok'})


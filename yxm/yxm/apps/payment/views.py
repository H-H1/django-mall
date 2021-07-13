import os

from alipay import AliPay
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models import OrderInfo


class PaymentView(APIView):
    """获取支付宝的支付链接"""

    def get(self, request, order_id):
        try:
            order = OrderInfo.objects.get(order_id=order_id,pay_method=OrderInfo.PAY_METHODS_ENUM["ALIPAY"],status=OrderInfo.ORDER_STATUS_ENUM["UNPAID"])
        except OrderInfo.DoesNotExist:
            return Response({"message":"订单信息有误"}, status=status.HTTP_400_BAD_REQUEST)

        app_private_key_string = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"keys/app_private_key.pem")).read() # 应用私钥
        alipay_public_key_string = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"keys/alipay_public_key.pem")).read() # 支付宝的公钥


        # 向支付宝发起请求 获取支付链接参数
        alipay = AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url=None, #默认回调url
            app_private_key_string=app_private_key_string,#
            alipay_public_key_string=alipay_public_key_string,#支付宝公钥
            sign_type="RSA2",
            debug=settings.ALIPAY_DEBUG,

        )

        # 手机网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id, #订单id
            total_amount=str(order.total_amount), #订单总金额
            subject="余希商城订单 %s" % order_id, #显示的名字
            return_url=settings.ALIPAY_RETURN_URL #支付完成回调地址 同步方式回调
        )
        print(order_string)
        # 支付地址的拼接
        alipay_url = settings.ALIPAY_URL + '?' + order_string
        print(alipay_url)

        # 拼接电脑支付的网址
        # 响应登录支付宝连接
        # 真实环境电脑网站支付网关：https://openapi.alipay.com/gateway.do? + order_string
        # 沙箱环境电脑网站支付网关：https://openapi.alipaydev.com/gateway.do? + order_string


        return Response({"alipay_url":alipay_url})


class PaymentStatusView(APIView):
    """保存支付结果"""
    def get(self, request):
        alipay_dict_data = request.query_params

        if not alipay_dict_data:
            return Response({"message":"支付回调参数有错误"}, status=status.HTTP_400_BAD_REQUEST)

        alipay_dict = alipay_dict_data.dict()#强制转换为字典
        print(alipay_dict)
        # 移除sign
        signature = alipay_dict.pop("sign") #商户请求参数的签名串

        app_private_key_string = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys/app_private_key.pem")).read()  # 应用私钥
        alipay_public_key_string = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys/alipay_public_key.pem")).read()  # 支付宝的公钥

        # 通知验证
        alipay = AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url=None,
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
            sign_type="RSA2",
            debug=settings.ALIPAY_DEBUG
        )

        # 通知验证
        success = alipay.verify(alipay_dict, signature)

        print('是否支付成功',success)
        print('签名串',signature)

        if success:
            # 保存订单支付状态和结果
            order_id = alipay_dict.get("out_trade_no")
            total_amount = alipay_dict.get("total_amount")
            trade_no = alipay_dict.get("trade_no")
            OrderInfo.objects.filter(order_id=order_id).update(status=OrderInfo.ORDER_STATUS_ENUM["UNSEND"])
            return Response({"trade_id":trade_no,"amount":total_amount})

        return Response({"message":"参数错误"}, status=status.HTTP_400_BAD_REQUEST)



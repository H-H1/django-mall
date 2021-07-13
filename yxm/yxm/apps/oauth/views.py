from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from oauth.OAuthQQAPIError import OAuthQQAPIError
from oauth.models import OAuthQQUser
from oauth.serializer import OauthQQuserSerilaier
from oauth.utils import OauthQQ


class QQAuthURLView(APIView):
    """获取QQ登录的网址"""
    def get(self, request):
        # 1. 获取?next参数
        next = request.query_params.get("next")
        # 2.去官方开发文档按照第一步的请求方法去得到响应数据里的登录网址
        oauth_qq = OauthQQ(state=next)
        login_url = oauth_qq.get_login_url()

        return Response({"login_url":login_url})


class QQAuthUserView(CreateAPIView):

    serializer_class = OauthQQuserSerilaier

    def get(self,request):
        # setp2. 获取Access Token
        # 1.获取code
        code = request.query_params.get("code")
        if not code:
            return Response({"message": "缺少code参数"}, status=status.HTTP_400_BAD_REQUEST)
        # 2.获取Access Token
        oauth_qq = OauthQQ()
        try:
            access_token = oauth_qq.get_access_token(code)
            # 3.获取openid
            openid = oauth_qq.get_openid(access_token)
        except OAuthQQAPIError:
            return Response({"message":"访问QQ官方接口异常"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        try:
            oauth_qq_user = OAuthQQUser.objects.get(openid=openid)
        except OAuthQQUser.DoesNotExist:
            # 如果openid在数据不存在，处理这个openid并返回
            a_token = oauth_qq.generate_bing_user_accesss_token(openid)
            return Response({"access_token":a_token})
        else:
            # 如果openid数据存在 表示这个用户之前已经绑定过，直接颁发token
            from rest_framework_jwt.settings import api_settings
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            user = oauth_qq_user.user
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            print(token)
            return Response({"token": token, "username":user.username, "user_id": user.id})

    # def post(self, request, *args, **kwargs):
    #     """创建新用户或绑定老用户账号"""




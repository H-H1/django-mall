import re

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.views import ObtainJSONWebToken

from carts.utlis import merge_cart_cookie_to_redis
from users import serializer, constants
from users.models import User
from users.serializer import UserDataiSerializer


class AddressViewSet(ModelViewSet): #功能很多的类
    """
    用户地址新增与修改
    """
    permissions = [IsAuthenticated]
    serializer_class = serializer.UserAddressSerializer


    def get_queryset(self): #根据addresses查询

        return self.request.user.addresses.filter(is_deleted=False)

    def list(self, request, *args, **kwargs):
        """
        用户地址列表数据
        """
        queryset = self.get_queryset()
        print(queryset,'66666666666666')
        serializer = self.get_serializer(queryset, many=True)
        user = self.request.user
        print(serializer.data)

        return Response({
            'user_id': user.id,
            'default_address_id': user.default_address_id,
            'limit': 10,
            'addresses': serializer.data,
        })
    def create(self, request, *args, **kwargs):
        """
        保存用户地址数据
        """
        # 检查用户地址数据数目不能超过上限
        count = request.user.addresses.count()
        print('ssssssssssssssssssssss')
        if count >= constants.USER_ADDRESS_COUNTS_LIMIT:
            return Response({'message': '保存地址数据已达到上限%s'%str(count)}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)



    #修改方法继承了 原来的父类方法,不在写
    def destroy(self, request, *args, **kwargs):
        """
        处理删除
        """
        address = self.get_object()
        print(address,'000000000000000')

        # 进行逻辑删除
        address.is_deleted = True
        address.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(methods=['put'], detail=True)
    def status(self, request, pk=None, address_id=None):
        """
        设置默认地址
        """
        address = self.get_object()
        request.user.default_address = address
        request.user.save()
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)

class VerifyEmailView(APIView):
    """
    邮箱验证
    """
    def get(self, request):
        # 获取token
        token = request.query_params.get('token')
        if not token:
            return Response({'message': '缺少token'}, status=status.HTTP_400_BAD_REQUEST)
        # 验证token
        user = User.check_verify_email_token(token)
        if user is None:
            return Response({'message': '链接信息无效'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.email_active =True
            user.save()
            return Response({'message': 'OK'})

# PUT /email/
class EmailView(UpdateAPIView):
    '''绑定邮箱'''

    permission_classes = [IsAuthenticated]
    serializer_class = serializer.EmailSerializer

    def get_object(self):
        return self.request.user
    # def put(self):
    #     # 获取email
    #     # 校验email
    #     # 查询user
    #     # 更新数据
    #     # 序列化返回






class UserRegView(CreateAPIView):
    '''
    用户注册视图类
    传入的数据
    '''
    serializer_class = serializer.CreateUserSerializer
    pass


class UsernameView(APIView):
    '查询用户的数量'

    def get(self, request, username):
        # 获取指定用户的数量
        count = User.objects.filter(username=username).count()
        data = {
            'username': username,
            "count": count

        }
        return Response(data)


class MobileView(APIView):
    "查询手机"

    def get(self, request, mobile):
        # 获取指定用户的数量
        count = User.objects.filter(mobile=mobile).count()
        data = {
            'username': mobile,
            "count": count
        }
        return Response(data)

    pass

class UserDataiView(RetrieveAPIView):
    # 1.判断是否获得认证权限,是否已经登录
    permission_classes = [IsAuthenticated]
    # 2使用序列化器
    serializer_class = UserDataiSerializer

    # 3返回当前请求对象的用户
    def get_object(self):
        return self.request.user

class UseraAuthView(ObtainJSONWebToken):
    '''登录认证'''
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        response=super().post(request, *args, **kwargs)

        if serializer.is_valid():
            user=serializer.validated_data['user']
            # 登陆时合并购物车
            print("登陆成功1")
            response = merge_cart_cookie_to_redis(request, user, response)
            print("登陆成功2")


        return response

class UserForgetView(UpdateAPIView):
    """找回密码"""

    def put(self, request, *args, **kwargs):
        req_data = request.data
        mobile = req_data['mobile']
        password = req_data['password']
        password2 = req_data['password2']
        sms_code = req_data['sms_code']

        # 1校验手机号码
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return Response({'message': '手机格式错误'}, status=status.HTTP_400_BAD_REQUEST)

        # 2校验两次输入的密码
        if password != password2:
            return Response({'message': '两次密码不一致'}, status=status.HTTP_400_BAD_REQUEST)

        # 3判断短信验证码
        redis_conn = get_redis_connection('verify_codes')
        real_sms_code = redis_conn.get('sms_%s' % mobile)
        if real_sms_code is None:
            return Response({'message': '无效的短信验证码'}, status=status.HTTP_400_BAD_REQUEST)
        if sms_code != real_sms_code.decode():
            return Response({'message': '短信验证码错误'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(mobile=req_data['mobile']).first()
        user.set_password(password)
        user.save()
        print("找回密码成功了",)
        return Response({'message': '找回密码成功'}, status=status.HTTP_201_CREATED)


    pass

#PUT 修改密码
class UserPwdView(UpdateAPIView):
    """修改密码"""
    # 1.判断权限
    permission_classes=[IsAuthenticated]
    #获取当前的请求用户
    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        #获取提交的数据
        req_data = request.data
        #验证原来的密码
        # 2.序列化器校验
        if not user.check_password(req_data['password']):
            return Response({'message':'原密码错误'}, status=status.HTTP_400_BAD_REQUEST)
        #3 。保存新的密码
        user.set_password(req_data['password2'])
        user.save()
        return Response({'message': '修改密码成功'}, status=status.HTTP_201_CREATED)


    pass




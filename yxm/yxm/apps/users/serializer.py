import re

from django.core.mail import send_mail
from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from celery_tasks.email.tasks import send_active_email
from users.models import User, Address
from yxm import settings
from yxm.settings.dev import EMAIL_FROM

class UserAddressSerializer(serializers.ModelSerializer):
    """
    用户地址序列化器
    """
    province = serializers.StringRelatedField(read_only=True)
    city = serializers.StringRelatedField(read_only=True)
    district = serializers.StringRelatedField(read_only=True)
    province_id = serializers.IntegerField(label='省ID', required=True)
    city_id = serializers.IntegerField(label='市ID', required=True)
    district_id = serializers.IntegerField(label='区ID', required=True)

    class Meta:
        model = Address
        exclude = ('user', 'is_deleted', 'create_time', 'update_time')

    def validate_mobile(self,value):
        #验证手机
        if not re.match(r'^1[3-9]\d{9}$',value):
            raise serializers.ValidationError("手机号格式错误")
        return value
    def create(self, validated_data):
        '''保存收货地址'''

        #系列化不能获得请求对象，只能从上下文获取

        validated_data['user'] = self.context['request'].user

        # Address.object.create(validated_data)
        return super().create(validated_data)



class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')
        extra_kwargs = {
            'email': {
                'required': True
            }
        }


    def update(self, instance, validated_data):
        """
        :param instance:  视图传过来的user对象
        :param validated_data:
        :return:
        """
        email = validated_data['email']

        instance.email = email
        instance.save()
        #发送邮件
        '''
        subject 邮件标题
        message 普通邮件正文， 普通字符串
        from_email 发件人
        recipient_list 收件人列表
        html_message 多媒体邮件正文，可以是html字符串
        '''


        '''创建一个模型链接'''
        url=instance.generate_verify_email_url()

        # subject = 'hyz'  # 邮件标题
        # from_email=EMAIL_FROM
        # html_message='<p>hyz</p>' \
        #              '邮箱：%s' \
        #              '<p><a href="%s">' \
        #              '点击</a></p>'%(email,url)
        # send_mail(subject=subject,from_email=from_email,message=html_message,recipient_list=[from_email])
        send_active_email(to_email=email,verify_url=url)

        return instance

class CreateUserSerializer(serializers.ModelSerializer):
    allow=serializers.CharField(label="用户协议",write_only=True)
    tuser=serializers.CharField(label="推广码",write_only=True,allow_blank=True)
    sms_code=serializers.CharField(label='短信验证码',write_only=True)
    token = serializers.CharField(label="JWT_toekn", read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'tuser', 'sms_code', 'mobile', 'allow', 'promocoer', 'promocode','token')
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 16,
                'error_messages': {
                    'min_length': '仅允许5-16个字符的用户名',
                    'max_length': '仅允许5-16个字符的用户名',
                }
            },
            'password': {
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的密码',
                    'max_length': '仅允许6-20个字符的密码',
                }
            },
            'tuser': {
                'max_length': 11,
                'error_messages': {
                    'max_length': '仅允许最大11个字符的推荐码',
                }
            }
        }

    def validate_mobile(self,value):
        #验证手机
        if not re.match(r'^1[3-9]\d{9}$',value):
            raise serializers.ValidationError("手机号格式错误")
        return value
    def validate_allow(self,value):
        #验证协议
        if value!='true':
            raise serializers.ValidationError("请同意协议")
        return value
    def validate(self, data):
        #验证短信


        mobile=data['mobile']
        sms_code=data['sms_code']
        redis_conn = get_redis_connection('verify_codes')
        redis_sms_code=redis_conn.get("sms_%s"%mobile)
        print(redis_sms_code)
        if redis_sms_code is None:
            raise serializers.ValidationError("验证码已失效")
        if redis_sms_code.decode() !=sms_code:
            raise serializers.ValidationError("验证码错误")
        return data


    def create(self, validated_data):
        '''创建用户'''
        print(validated_data)
        del validated_data['sms_code']
        del validated_data['allow']
        promocode=validated_data["tuser"]
        mobile=validated_data["mobile"]
        try:
            tj_user=User.objects.get(promocode=promocode)
            # print(tj_user,'++++++++++++++++++++++++++++')
        except User.DoesNotExist:
            validated_data["promocoer"]=0
        else:
            validated_data['promocoer']=tj_user.id

        del validated_data['tuser']
        print(validated_data)
        # User.objects.create(**validated_data)#1.使用模块创建方法

        user=super().create(validated_data) #2.serializers.ModelSerializer父类的创建方法
        user.set_password(validated_data['password'])#加密密码
        user.save()

        #颁发令牌
        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # payload = jwt_payload_handler(user)
        # token = jwt_encode_handler(payload)

        # user.token = token
        user.token = api_settings.JWT_ENCODE_HANDLER(api_settings.JWT_PAYLOAD_HANDLER(user))


        return user

class UserDataiSerializer(serializers.ModelSerializer):
    avatar_img=serializers.CharField(read_only=True)
    class  Meta:
        model=User
        fields=('id','username','mobile','email','email_active','avatar_img')

    pass







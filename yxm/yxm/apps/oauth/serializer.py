from django_redis import get_redis_connection
from rest_framework import serializers

from oauth.models import OAuthQQUser
from oauth.utils import OauthQQ
from users.models import User


class OauthQQuserSerilaier(serializers.ModelSerializer):
    """QQ绑定注册的序列化器"""
    tuser = serializers.CharField(label="推荐码", write_only=True, allow_blank=True, allow_null=True)
    sms_code = serializers.CharField(label="短信验证码", write_only=True)
    token = serializers.CharField(label="JWT_toekn", read_only=True)
    access_token = serializers.CharField(label="操作凭证", write_only=True)
    mobile = serializers.RegexField(label="手机号",regex=r'^1[3-9]\d{9}$')

    class Meta:
        model = User
        fields = ("id","username","tuser","mobile","sms_code","access_token","password","token","promocode","promocoer")
        extra_kwargs = {
            'username': {"read_only":True},
            'password': {
                'write_only': True,  # 密码不对外输出
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

    def validate(self, data):
        # 验证短信验证码
        print(data)
        access_token = data["access_token"]
        #验证openid是否正确
        openid = OauthQQ.check_bing_user_accesss_token(access_token) # open  or  None
        if not openid:
            raise serializers.ValidationError("无效的access_token")
        data["openid"] = openid

        mobile = data["mobile"]
        sms_code = data["sms_code"]
        redis_conn = get_redis_connection("verify_codes")
        # 去redis查询短信验证码
        redis_sms_code = redis_conn.get("sms_%s" % mobile)
        print(redis_sms_code)
        if redis_sms_code is None:
            raise serializers.ValidationError("短信验证码已经失效！")
        if redis_sms_code.decode() != sms_code:
            raise serializers.ValidationError("短信验证码错误！")
        # 如果用户存在，要验证手机对应的密码是否正确
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            pass
        else:
            password = data["password"]
            if not user.check_password(password):
                raise serializers.ValidationError("密码错误")
            data["user"] = user
        return data

    def create(self, validated_data):
        """重写创建方法"""
        print(validated_data)
        openid = validated_data["openid"]
        mobile = validated_data["mobile"]
        password = validated_data["password"]
        promocode = validated_data["tuser"]

        try:
            tj_user = User.objects.get(promocode=promocode)
        except User.DoesNotExist:
            # promocode=mobile
            promoter = 0
        else:
            promoter = tj_user.id


        user = validated_data.get("user")  # user or None
        if not user:
            # 创建新用户
            '''create_user会自动加密密码'''
            user = User.objects.create_user(username=mobile, mobile=mobile, password=password,promocode=mobile,promocoer=promocode)
        # 绑定QQ登录
        OAuthQQUser.objects.create(openid=openid, user=user)

        # TOKEN 颁发令牌
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        print(token)
        user.token = token

        return user


#from django.contrib.auth.backends import ModelBackend
import re

from django.contrib.auth.backends import ModelBackend

from users.models import User


def jwt_response_payload_handler(token,request=None,user=None):
    data={'user_id':user.id,'username':user.username,"token":token}
    return data
# def jwt_response_payload_handler(token, user=None, request=None):
#     """
#     自定义jwt认证成功返回数据
#     """
#     return {
#         'token': token,
#         'user_id': user.id,
#         'username': user.username
#     }

def get_user_by_account(account):
    '''
    根据账账号获取用户名
    :param account: 可以是手机或用户名
    :return:
    '''
    try:
        if re.match("^1[2-9]\d{9}",account):
            #账号为手机号
            user=User.objects.get(mobile=account)
        else:
            #账号为用户名
            user=User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user
class UsernameMobileAuthBackend(ModelBackend):
    """
    重写 自定义用户名或手机号认证也可以登录系统
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password):
            return user

import json
import urllib, logging
from urllib.request import urlopen
from django.conf import settings

from oauth.constants import BIND_USER_ACCESS_TOKEN_EXPIRES
from oauth.OAuthQQAPIError import OAuthQQAPIError
from itsdangerous import BadData, TimedJSONWebSignatureSerializer as TJWSerializer

logger = logging.getLogger("django")

class OauthQQ(object):
    """QQ辅助工具"""
    def __init__(self,client_id=None, client_secret=None, redirect_uri=None, state=None):
        """
        :param client_id: QQ_CLIENT_ID
        :param client_secret: QQ_CLIENT_SECRET
        :param redirect_uri: QQ_REDIRECT_URI
        :param state: QQ_STATE
        """
        self.client_id = client_id if client_id else settings.QQ_CLIENT_ID
        self.client_secret = client_secret if client_secret else settings.QQ_CLIENT_SECRET
        self.redirect_uri = redirect_uri if redirect_uri else settings.QQ_REDIRECT_URI
        self.state = state or settings.QQ_STATE
    # 第1步
    def get_login_url(self):
        '''获取Authorization_Code'''
        # url = "https://graph.qq.com/oauth2.0/authorize?response_type={}&client_id={}".format(????)
        url = "https://graph.qq.com/oauth2.0/authorize?"
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state":self.state

        }
        url += urllib.parse.urlencode(params)
        print('======',url)
        print(self.client_id)
        print(self.redirect_uri)
        print(self.state)
        return url

    # 第2步
    def get_access_token(self,code):
        '''通过Authorization_Code获取access_Token'''
        url = "https://graph.qq.com/oauth2.0/token?"
        params = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "redirect_uri": self.redirect_uri
        }
        url += urllib.parse.urlencode(params) #将query字典转换为url路径中的查询字符串
        try:
            resp = urlopen(url)
            '''
            urllib.request.urlopen(url, data=None)

            发送http请求，如果data为None，发送GET请求，如果data不为None，发送POST请求

            返回response响应对象，可以通过read()读取响应体数据，需要注意读取出的响应体数据为bytes类型
            '''


            resp_str = resp.read().decode()
            print(resp_str)

            resp_dict = urllib.parse.parse_qs(resp_str)#将qs查询字符串格式数据转换为python的字典

            print(resp_dict)
            print(self.client_id)
            print(self.redirect_uri)
            print(self.state)
        except Exception as e:
            logger.error("获取access_token异常 %s" % e)
            raise OAuthQQAPIError
        else:
            access_token = resp_dict.get("access_token")
            print(access_token)

            return access_token[0]

    # 第3步
    def get_openid(self,accesss_token):
        '''通过获取access_token获取openid'''
        url = "https://graph.qq.com/oauth2.0/me?access_token=" + accesss_token
        try:
            resp_str = urlopen(url).read().decode()
            print(resp_str) # callback( {"client_id":"YOUR_APPID","openid":"YOUR_OPENID"} );
            resp_str = resp_str[10:-4]
            print(resp_str)
            resp_dict = json.loads(resp_str)
            print(resp_dict)

        except Exception as e:
            logger.error("获取openid异常 %s" % e)
            raise OAuthQQAPIError
        else:
            openid = resp_dict.get("openid")
            print(openid)

            return openid

    # 加密openid
    def generate_bing_user_accesss_token(self,openid):
        s = TJWSerializer(settings.SECRET_KEY, BIND_USER_ACCESS_TOKEN_EXPIRES)
        token = s.dumps({"openid":openid})
        print(token)
        token = token.decode()
        return token
    #解密openid
    @staticmethod
    def check_bing_user_accesss_token(access_token):
        s = TJWSerializer(settings.SECRET_KEY, BIND_USER_ACCESS_TOKEN_EXPIRES)
        try:
            data = s.loads(access_token)
            print(data)
        except BadData:
            logging.error('  {}  解码超时'.format(access_token))
            return None
        return data["openid"]







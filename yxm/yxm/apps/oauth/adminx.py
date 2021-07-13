import xadmin

from oauth.models import OAuthQQUser

class QAuthQQUserAdmin:
    '''QQ绑定'''
    list_display=['user','openid']

xadmin.site.register(OAuthQQUser,QAuthQQUserAdmin)
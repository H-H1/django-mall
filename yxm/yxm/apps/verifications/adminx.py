import xadmin
from xadmin import views
from verifications.views import SmsSendlog
class GlobalSetting(object):
    site_title="商城后台管理"
    site_footer='后台公司'
    menu_style='accordion'
class BaseSetting:
    '''基本设置'''
    enable_themes=True #主题开关
    use_bootswatch=True
class SmsSendLogAdmin:
    list_display=['id','mobile','code','create_time']
#相当于重写这个类,添加字段或选择
xadmin.site.register(views.CommAdminView,GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(SmsSendlog,SmsSendLogAdmin)

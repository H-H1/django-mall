from django.urls import re_path

from oauth import views

urlpatterns = [
    re_path(r'qq/authorization/',views.QQAuthURLView.as_view()), #登录网址
    re_path(r'qq/user/',views.QQAuthUserView.as_view()), # 获取Access Token

]
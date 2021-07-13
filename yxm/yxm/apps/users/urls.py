from django.urls import re_path
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token
from users import views

urlpatterns=[
    re_path(r'^usernames/(?P<username>\w{5,16})/count/$',views.UsernameView.as_view()), #查询用户名
    re_path(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$',views.MobileView.as_view()), #查询手机
    re_path(r'^users/$',views.UserRegView.as_view()),#创建用户手机
    re_path(r'^user/$',views.UserDataiView.as_view()), #用户信息
    # re_path(r'^authorizations/',obtain_jwt_token) #用户信息
    re_path(r'^authorizations/$',views.UseraAuthView.as_view()), #用户信息
    re_path(r'^users/pwd/$',views.UserPwdView.as_view()),#用户信息,
    re_path(r'^users/forget/$',views.UserForgetView.as_view()), #用户信息,
    re_path(r'^email/$',views.EmailView.as_view()), #用户信息,
    re_path(r'^emails/verification/$',views.VerifyEmailView.as_view()), #用户信息,

]
router = SimpleRouter()
router.register(r'addresses', views.AddressViewSet, basename='addresses')

urlpatterns += router.urls

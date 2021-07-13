from django.urls import re_path
from payment import views
urlpatterns = [
    re_path(r'^orders/(?P<order_id>\d+)/payment/$', views.PaymentView.as_view()), # 跳转到支付宝的支付页面
    re_path(r'^payment/status/$', views.PaymentStatusView.as_view()),  # 保存支付结果

]
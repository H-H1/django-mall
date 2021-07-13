from django.urls import re_path
from orders import views
urlpatterns = [
    re_path(r'^orders/settlement/$', views.OrderSettlementView.as_view()),
    re_path(r'^orders/$', views.SaveOrderView.as_view()),
]
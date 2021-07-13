from django.urls import re_path
from carts import views
from django.urls import re_path
from carts import views
urlpatterns = [
    re_path(r'^cart/$', views.CartView.as_view()),
    re_path(r'^cart/selection/$', views.CartSelectAllView.as_view()),
]
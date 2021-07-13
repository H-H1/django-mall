"""yxm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),#富文本编辑器
    path('',include('verifications.urls')),
    path('',include('users.urls')),
    path('',include('area.urls')),
    path('',include('feedback.urls')),
    path('oauth/',include('oauth.urls')),
    path('',include('goods.urls')),
    path('',include('carts.urls')),
    path('',include('orders.urls')),
    path('',include('payment.urls')),
]

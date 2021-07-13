from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
# Create your views here.
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Area
from .serializers import AreaSerializer, SubAreaSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin
# centos需要安装setuptools-scm,管理版本冲突

class AreasViewSet(CacheResponseMixin,ReadOnlyModelViewSet): #缓存视图，区划视图
    """
    行政区划信息
    """
    pagination_class = None  # 区划信息不分页

    def get_queryset(self):
        """
        提供数据集,查询省级行政（父级）
        """
        if self.action == 'list':
            return Area.objects.filter(parent=None) #127.0.0.1/areas/ --如何查询的是list
        else:
            return Area.objects.all()

    def get_serializer_class(self):
        """
        提供序列化器
        """
        if self.action == 'list':
            return AreaSerializer  #127.0.0.1/areas/
        else:
            return SubAreaSerializer #127.0.0.1/areas/4300000/ --如果查询的是详细数据
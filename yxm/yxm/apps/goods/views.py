from django.shortcuts import render

# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.cache.mixins import ListCacheResponseMixin
from rest_framework.filters import OrderingFilter
from goods.models import Brand, GoodsCategory, Goods, SKU
from goods.serializer import BrandSerializer, CategorySerializer, SKUSerializer, SKUIndexSerializer
from yxm.utils.exceptions import logger
from drf_haystack.viewsets import HaystackViewSet



class BrandListView(ListAPIView):
    """品牌数据"""
    serializer_class = BrandSerializer

    def get_queryset(self):
        try:
            data = Brand.objects.filter(brand_apply=True, brand_recommend=True).order_by('-brand_sort')
        except Exception as e:
            logger.error(e)

        return data


class CategoryListView(ListAPIView):
    """品牌数据"""
    serializer_class = CategorySerializer

    def get_queryset(self):
        try:
            data = GoodsCategory.objects.filter(c_apply=True, parent=None).order_by('-csort')
        except Exception as e:
            logger.error(e)

        return data


class CgoryListView(APIView):
    """子类(其他)数据"""

    def get(self, request, pk):

        # 二级数据
        try:
            queryset_data = GoodsCategory.objects.filter(c_apply=True, parent_id=pk).order_by('-csort')
            # print(queryset_data)
        except Exception as e:
            logger.error(e)

        category_list = []

        for cg in queryset_data:
            category_dict = {}
            try:
                sub_data = GoodsCategory.objects.filter(c_apply=True, parent_id=cg.id).order_by('-csort')
            except Exception as e:
                logger.error(e)
            # print('sub',sub_data)
            sub_list = []
            for sg in sub_data:
                sub_dict = {}
                sub_dict['id'] = sg.id
                sub_dict['name'] = sg.name
                sub_dict['clogo'] = sg.clogo.url
                sub_list.append(sub_dict)
            category_dict['id'] = cg.id
            category_dict['name'] = cg.name
            category_dict['clogo'] = cg.clogo.url
            category_dict['sub'] = sub_list
            category_list.append(category_dict)
        # print(category_list)
        return Response(category_list)


class SKUBrandListView(ListAPIView):
    '''品牌商品列表数据'''
    serializer_class = SKUSerializer
    filter_backends = [OrderingFilter]
    ordering_fiter = ("id", 'price', 'sales', 'create_time')  # 按指定的字段进行排序

    def get_queryset(self):
        brand_id = self.request.query_params.get('brand')  # 查询"？"后的字符串
        try:
            if brand_id:
                goods_data = Goods.objects.filter(brand_id=brand_id)
                goods_list = []
                for goods in goods_data:
                    goods_list.append(goods.id)

                print(goods_list)

                sku_data = SKU.objects.filter(is_launched=True, goods_id__in=goods_list)  # '__id' 可以遍历列表
                print('sku_data', sku_data)
            else:
                return []
        except Exception as e:
            logger.error(e)
            return []
        return sku_data


class SKUListView(ListAPIView):
    """
    商品列表视图
    """
    serializer_class = SKUSerializer
    # queryset = SKU.objects.filter(category=???)

    # 排序
    filter_backends = [OrderingFilter]
    ordering_fields = ('create_time', 'price', 'sales')

    # 分页, 全局设置

    def parse_cg(self, cg_id):
        cg_list = []
        if cg_id:
            cg_list_data = GoodsCategory.objects.filter(parent_id=cg_id)

            if cg_list_data:
                for c in cg_list_data:
                    cg_list.append(c.id)
                    c__id=self.parse_cg(c.id)
                    print(c__id)
                    cg_list += c__id# 递归查询该id的"子类"

            return cg_list

    def get_queryset(self):
        category_id = self.request.query_params.get('id')
        try:
            if not category_id:
                data = SKU.objects.filter(is_launched=True)
            else:
                # cg_list = [int(category_id), ]
                cg_list = self.parse_cg(category_id)
                print(cg_list)
                cg_list.insert(0, int(category_id))
                # print(cg_list)
                data = SKU.objects.filter(category_id__in=cg_list, is_launched=True)
        except Exception as e:
            logger.error(e)
            return []

        return data

class SKUSearchViewSet(HaystackViewSet):
    """
    SKU搜索
    """

    index_models = [SKU]
    serializer_class = SKUIndexSerializer

class StandardResultsSetPagination(PageNumberPagination):
    # 默认每页条数`
    page_size = 4

    # 前端访问指明每页数量的参数名
    page_size_query_param = 'page_size'

    # 限制前端指明每页数量的最大限制
    max_page_size = 20

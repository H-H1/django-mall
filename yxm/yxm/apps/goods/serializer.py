from goods.models import Brand, GoodsCategory, SKU
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    """品牌序列化器"""
    class Meta:
        model = Brand
        fields = ('id', 'name', 'logo')



class CategorySerializer(serializers.ModelSerializer):
    """分类序列化器"""
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name', 'clogo')



class SKUSerializer(serializers.ModelSerializer):
    '''商品列表序列化器'''
    class Meta:
        model = SKU
        fields=('id','name','default_image_url','price','comments','create_time')



from drf_haystack.serializers import HaystackSerializer
from goods.search_indexes import SKUIndex

class SKUIndexSerializer(HaystackSerializer):
    """SKU索引结果数据序列化器"""
    class Meta:
        index_classes = [SKUIndex]
        filter = ('text','id','name','price','comments','default_image_url')
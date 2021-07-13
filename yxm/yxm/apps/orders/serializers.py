import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from django_redis import get_redis_connection
from rest_framework import serializers
from goods.models import SKU
from orders.models import OrderInfo, OrderGoods

logger = logging.getLogger("django")

class CartSKUSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(label="数量", min_value=1)

    class Meta:
        model = SKU
        fields = ("id", "name", "count", "price", "default_image_url")


class OrderSettlementSerializer(serializers.Serializer):
    freight = serializers.DecimalField(label="运费", max_digits=10, decimal_places=2)
    skus = CartSKUSerializer(many=True)


class OrderSaveSerializer(serializers.ModelSerializer):
    """订单的保存"""
    class Meta:
        model = OrderInfo
        fields = ("address","pay_method","order_id")
        read_only_fields = ("order_id",)
        extra_keargs = {
            "address":{"write_only":True},
            "pay_method":{"required":True}
        }

    def create(self, validatated_data):
        """保存"""
        print(validatated_data)
        address = validatated_data["address"]
        pay_method = validatated_data["pay_method"]
        # 获取请求对象的用户
        user = self.context['request'].user # 在序列化器里只能通过请求上下文得到请求对象

        # 从redis中查询购物车 selected sku_id count
        redis_conn = get_redis_connection("cart")
        # 哈希
        redis_cart = redis_conn.hgetall("cart_%s" % user.id)  # DICT
        # 集合
        redis_cart_selected = redis_conn.smembers("cart_selected_%s" % user.id)  # SET
        cart = {}
        for sku_id in redis_cart_selected:
            cart[int(sku_id)] = int(redis_cart[sku_id])

        print(cart)

        if not cart:
            raise serializers.ValidationError("没有需要结算的商品")

        # 创建一个保存节点
        save_id = transaction.savepoint()
        # 保存订单信息
        order_id = timezone.now().strftime("%Y%m%d%H%M%S") + ("%06d" % user.id)
        print(order_id)

        # 保存订单商品的数据
        try:
            order = OrderInfo.objects.create(
                order_id=order_id,
                user=user,
                address=address,
                total_count=0,
                total_amount=Decimal(0),
                freight=Decimal("10.00"),
                pay_method=pay_method,
                status= OrderInfo.ORDER_STATUS_ENUM["UNSEND"] if pay_method==OrderInfo.PAY_METHODS_ENUM["CASH"] else OrderInfo.ORDER_STATUS_ENUM["UNPAID"]
            )

            # 遍历结算商品
            sku_id_list = cart.keys()
            for sku_id in sku_id_list:
                while True:
                    # 判断商品库存是否充足
                    sku = SKU.objects.get(id=sku_id)
                    origin_stock = sku.stock # 原始的库存
                    origin_sales = sku.sales # 原始的销量
                    # 当前这个商品购买的数量
                    sku_count = cart[sku.id]
                    print(sku_count)
                    if sku_count > origin_stock: # 当时的数据 需要事务处理
                        # 购买的库存不足
                        # 返回序列化异常
                        transaction.savepoint_rollback(save_id)
                        raise serializers.ValidationError("库存不足")
                    # 减少商品库存，增加商品销量
                    new_stock = origin_stock - sku_count
                    new_sales = origin_sales + sku_count
                    # sku.stock =new_stock
                    # sku.sales =new_sales
                    # sku.save()
                    # 用乐观锁去修改订单的数据
                    sku_obj_count = SKU.objects.filter(id=sku_id,stock=origin_stock).update(stock=new_stock,sales=new_sales)
                    if sku_obj_count == 0:
                        # 结束本次循环，进行洗一次循环
                        continue
                    # 修改Goods总销量
                    sku.goods.sales += sku_count
                    sku.goods.save()
                    # 修改订单的总金额和总数量
                    order.total_count += sku_count
                    order.total_amount += (sku.price * sku_count)
                    # order.save()要在循环结束后再去保存
                    # 保存订单商品的信息
                    OrderGoods.objects.create(
                        order=order,
                        sku=sku,
                        count=sku_count,
                        price=sku.price
                    )
                    break
                order.save()

        except serializers.ValidationError:
            raise
        except Exception as e:
            logger.error(e)
            #  事务的回滚
            transaction.savepoint_rollback(save_id)
            raise
        else:
            # 事务的提交
            transaction.savepoint_commit(save_id)

        # 删除购物车已提交的数据
        pl = redis_conn.pipeline()
        # 删除hash数据
        pl.hdel("cart_%s" % user.id, *redis_cart_selected) # 解包
        # 删除set数据
        pl.srem("cart_selected_%s" % user.id, *redis_cart_selected)
        pl.execute()

        return order

class SaveOrderSerializer(serializers.ModelSerializer):
    """
    保存订单序列化器
    """
    class Meta:
        model = OrderInfo
        fields = ('address', 'pay_method', 'order_id')
        read_only_fields = ('order_id',)
        extra_kwargs = {
            'address': {
                'write_only': True
            },
            'pay_method': {
                'required': True
            }
        }

    def create(self, validated_data):
        """保存订单"""
        pass
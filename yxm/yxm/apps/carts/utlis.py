import pickle
import base64
from django_redis import get_redis_connection


def merge_cart_cookie_to_redis(request, user, response):
    """
    合并请求用户的购物车数据，将未登录保存在cookie里的保存到redis中
    :param request: 用户的请求对象
    :param user: 当前登录的用户
    :param response: 响应对象，用于清楚购物车cookie
    :return:
    """
    cookie_cart = request.COOKIES.get('cart')
    if not cookie_cart:
        print('没cookie')
        return response

    cookie_cart_dict = pickle.loads(base64.b64decode(cookie_cart.encode()))
    print(cookie_cart_dict)

    #  获取到redis数据
    redis_conn = get_redis_connection("cart")

    redis_cart = redis_conn.hgetall("cart_%s" % user.id) # sku_id,count
    redis_cart_selected = redis_conn.smembers('cart_selected_%s' % user.id)

    print("----------------")
    print(redis_cart)
    print(redis_cart_selected)
    print("----------------")

    cart = {}
    for sku_id,count in redis_cart.items():
        cart[int(sku_id)] = int(count)

    redis_cart_selected_add = []
    redis_cart_selected_remove = []

    for sku_id,count_selected_dict in cookie_cart_dict.items():
        # 处理商品的数量
        cart[sku_id] = count_selected_dict['count']
        if count_selected_dict['selected']:
            #勾选
            redis_cart_selected_add.append(sku_id)
        else:
            redis_cart_selected_remove.append(sku_id)
        print(redis_cart_selected_add)
        print(redis_cart_selected_remove)
        if cart:
            pl = redis_conn.pipeline()
            # pl. 哈希 和集合的数据的写入
            pl.hmset("cart_%s" % user.id, cart)

            if redis_cart_selected_remove:
                pl.srem("cart_selected_%s" % user.id, *redis_cart_selected_remove)
            if redis_cart_selected_add:
                pl.sadd("cart_selected_%s" % user.id, *redis_cart_selected_add)
            pl.execute()
        # 清空cookie里的购物数据
        response.delete_cookie('cart')
        print("清空cookie购物车数据成功")

        return response
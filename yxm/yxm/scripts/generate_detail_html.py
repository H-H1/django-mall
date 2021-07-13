import os,sys

print(sys.path)
sys.path.insert(0,"../")
sys.path.insert(0,"../../")
sys.path.insert(0,"../yx_mall/apps")
print("-"*30)

print(sys.path)

if not os.getenv("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = "yxm.settings.dev"

import django
django.setup() # django初始化

from django.conf import settings
from django.template import loader
from goods.models import SKU


def generate_static_sku_detail_html(sku_id):
    """生成商品详情静态页"""
    try:
        sku = SKU.objects.get(id=sku_id)
    except Exception as e:
        print(e)

    contexts = {
        "sku_id":sku.id,
        "sku_name":sku.name,
        'sku_price':sku.price,
        'sku_sales':sku.sales,
        'sku_caption':sku.caption,
        'sku_stock':sku.stock,
        'sku_url':sku.default_image_url,
        'sku_comments':sku.comments,
    }
    print(contexts)



    template = loader.get_template("temp_detail.html")

    html_text = template.render(contexts)

    # 位置(商品详情页面id.html 文件保存位置)
    index_path_file = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR, "wap/shop/goods/" + str(sku_id) + ".html")

    print("生成商品详情页文件中……")
    with open(index_path_file, "w", encoding="utf-8") as f:
        f.write(html_text)

if __name__ == '__main__':
    skus = SKU.objects.all()
    for sku in skus:
        print(sku.id)
        print("开始批量生成所有商品的详情页面")
        generate_static_sku_detail_html(sku.id)


# 作业2
""" 练习模板 把temp_detail补充完整"""

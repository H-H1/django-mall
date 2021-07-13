import os
import time

from django.conf import settings
from django.template import loader

from goods.models import SKU


def generate_static_index_html():
    """
    生产静态首页 http://demo.myuxi.wang/index.html
    :return:
    """
    # 查询各个数据表的数据 组成复杂的数据
    print('%s: generate_static_index_html' % time.ctime())
    goods = SKU.objects.filter(is_launched=True).order_by("-update_time")
    contexts = {
        'goods': goods
    }
    # 制定一个首页的模板
    template = loader.get_template('temp_index.html')

    # 模板的渲染数据 用with open 写入这个index.html文件
    html_text = template.render(contexts)

    temp_path = os.path.join(settings.GENERATED_STATIC_HTML_FILES_DIR, 'index.html')
    print(temp_path)
    print("生成文件")

    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(html_text)
import os,sys

print(sys.path)
sys.path.insert(0,"../yx_mall/apps") #修改文件目录。提高导包速度
print("-"*30)

print(sys.path)

if not os.getenv("DJANGO_SETTINGS_MODULE"):
    os.environ["DJANGO_SETTINGS_MODULE"] = "yxm.settings.dev"

import django
django.setup() # django初始化

if __name__ == '__main__':
    from contents.crons import generate_static_index_html
    generate_static_index_html()
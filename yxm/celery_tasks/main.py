
from celery import Celery

import os
print(os.getenv('DJANGO_SETTINGS_MODULE'))
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE']='yxm.settings.dev'

#创建一个celert应用
celery_app=Celery('yxm')
#导入celery配
celery_app.config_from_object('celery_tasks.config')
#导入任务

celery_app.autodiscover_tasks(['celery_tasks.sms', 'celery_tasks.email'])


'''
创建文件夹
~/Desktop/yxm$ sudo mkdir /var/run/celery
               sudo chmod 777 /var/run/celery


启动
~/Desktop/yxm/yxm$ celery -A celery_tasks.main worker -l info 
守护运行
celery multi start wl -A  celery_tasks.main worker -l info --logfile=./celery.log

'''
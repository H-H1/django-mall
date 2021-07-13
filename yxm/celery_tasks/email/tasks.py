from django.conf import settings
from django.core.mail import send_mail


from celery_tasks.main import celery_app

import logging


logger = logging.getLogger('django')

@celery_app.task(name='send_active_email')
def send_active_email(to_email, verify_url):
    print('task================')
    subject = "余惜商城邮箱验证"
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用余惜商城。</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)
    send_mail(subject, "", settings.EMAIL_FROM, [to_email], html_message=html_message)
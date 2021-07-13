from rest_framework.response import Response

from celery_tasks.main import celery_app
from celery_tasks.sms.sms import SMSC
import logging


logger = logging.getLogger('django')

@celery_app.task(name="send_sms_code")
def send_sms_code(mobile, sms_code):
    try:
        rest = SMSC(mobile, sms_code)
    except Exception as e:
        logger.error("%s 发送短信验证"%mobile)
        return Response({'message':'发送短信失败'})
    else:
        if rest=='1':
            logger.info('发生短信验证码【成功】【mobile：%s】'%mobile)
        else:
            logger.info('发送短信验证码【失败】【moblie:%s】'%mobile)



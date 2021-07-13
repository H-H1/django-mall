import re

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from itsdangerous import TimedJSONWebSignatureSerializer, BadData

from yxm.utils.models_time import BaseModel


class User(AbstractUser):
    "用户模型类"

    mobile=models.CharField(verbose_name="手机号",max_length=11,unique=True)
    promocode=models.CharField(verbose_name="推广码",max_length=11,blank=True,null=True,unique=True)
    promocoer=models.CharField(verbose_name="推广人ID",default=0,max_length=11)
    email_active = models.BooleanField(verbose_name='邮箱验证状态',default=False)
    avatar=models.ImageField(verbose_name="头像图片",null=True,blank=True,upload_to=['avatar'])
    #字段名user不能重复
    default_address = models.ForeignKey('Address', related_name='u', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='默认地址')


    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def avatar_img(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/static/images/member.png"

    def generate_verify_email_url(self):
        """生成验证邮箱的url"""
        s = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, expires_in=24 * 3600 *7)
        data = {"user_id":self.id, "email": self.email}
        token = s.dumps(data).decode()

        verify_url = "http://mm.yxmm.com/verify_email.html?token=" + token

        return verify_url
    @staticmethod
    def check_verify_email_token(token):
        s = TimedJSONWebSignatureSerializer(settings.SECRET_KEY, expires_in=24 * 3600 * 7)
        try:
            data = s.loads(token)
        except BadData:
            return None
        else:
            user_id = data['user_id']
            email = data['email']
            try:
                user = User.objects.get(id=user_id, email=email)
            except User.DoesNotExist:
                return None
            else:
                return user

class Address(BaseModel):
    """
    用户的收货地址
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='用户')
    # title = models.CharField(max_length=20, verbose_name='地址名称')
    receiver = models.CharField(max_length=20, verbose_name='收货人')
    province = models.ForeignKey('area.Area', on_delete=models.PROTECT, related_name='province_addresses', verbose_name='省')
    city = models.ForeignKey('area.Area', on_delete=models.PROTECT, related_name='city_addresses', verbose_name='市')
    district = models.ForeignKey('area.Area', on_delete=models.PROTECT, related_name='district_addresses', verbose_name='区')
    place = models.CharField(max_length=50, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    email = models.CharField(max_length=30, null=True, blank=True, default='', verbose_name='电子邮箱')
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_address'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name
        ordering = ['-update_time'] # 排序按更新时间降序

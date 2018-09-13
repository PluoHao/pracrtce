from django.db import models

# Create your models here.

class USER(models.Model):
    uname = models.CharField('用户名',max_length=50,null=False)
    upassword = models.CharField('密码',max_length=200,null=False)
    uphone = models.CharField('手机号',max_length=11,null=False)
    identity = models.CharField('身份证',max_length=18,null=False)
    isactive = models.BooleanField('状态',default=True)

    def __str__(self):
        return self.uname
    class Meta:
        db_table = 'USER'
        verbose_name_plural = '用户'


class Address(models.Model):
    Aname = models.CharField('收货人',max_length=50,null=False)
    Aphone = models.CharField('手机',max_length=11,null=False)
    ADS = models.CharField('地址',max_length=200,null=False)
    orderId = models.CharField('订单号',max_length=30,null=False)
    USER = models.ForeignKey(USER)

    def __str__(self):
        return self.orderId
    class Meta:
        db_table = 'Address'
        verbose_name_plural = '地址'

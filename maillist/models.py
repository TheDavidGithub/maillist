# coding=UTF-8
from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=45, null=False, verbose_name=u'用户名')
    password = models.CharField(max_length=45, null=False, verbose_name=u'密码')

    def __unicode__(self):
        return u'{0}'.format(self.username)

    class Meta:
        unique_together = ('username',)
        db_table = 'users'


class PhoneNumber(models.Model):
    user_id = models.IntegerField(null=False, verbose_name=u'用户id,对应Users表的id')
    info_id = models.IntegerField(null=False, verbose_name=u'某用户的通讯录的某信息的编号')
    name = models.CharField(max_length=45, null=True, verbose_name=u'联系人名称')
    phone = models.IntegerField(null=True, verbose_name=u'联系人电话号码')

    def __unicode__(self):
        return u'{0} {1} {2} {3}'.format(self.user_id, self.info_id, self.name, self.phone)

    class Meta:
        unique_together = ('user_id', 'info_id')
        db_table = 'phone_number'

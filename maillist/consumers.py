# -*- coding:UTF-8 -*-
import json
from channels import Group
from channels.sessions import channel_session
from maillist.models import Users, PhoneNumber


@channel_session
def ws_connect(message):
    pass


@channel_session
def ws_receive(message):
    data = json.loads(message['text'])
    user_id = data.get('user_id')
    # 用户在任意设备登录时增加一条信道
    if data.get('send_type') == 'connect':
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            print 'Does not exist user_id=%s' % user_id
            return
        # mail-1代表用户id为1的用户的通信通道
        Group('mail-%s' % user_id).add(message.reply_channel)
        message.channel_session['user'] = user.id
        print 'user %s connected' % user_id
    # 用户发送数据，用于同步等
    if data.get('send_type') == 'send_info':
        syn_phone_num(message)


@channel_session
def ws_disconnect(message):
    # 断开对应用户的所有信道连接
    user_id = message.channel_session['user']
    Group('mail-%s' % user_id, channel_layer=message.channel_layer).discard(message.reply_channel)


def syn_phone_num(message):
    data = json.loads(message['text'])
    if data.get('info_id') is None:
        to_return = {
            'result': 'fail',
            'msg': '请输入info_id！'
        }
        message.reply_channel.send({'text': json.dumps(to_return)})
    else:
        # 用户编辑的状态：新增、删除、修改
        status = data.get('status')
        # 用户编辑前的数据，用于与数据库的最新数据作对比
        old_data = data.get('old_data')
        # 获得数据库的最新的数据
        last_data = PhoneNumber.objects.filter(
            user_id=data.get('user_id'),
            info_id=data.get('info_id')
        ).all()
        if status == 'delete':
            if last_data:
                PhoneNumber.objects.filter(
                    user_id=data.get('user_id'),
                    info_id=data.get('info_id')
                ).delete()
                to_return = {
                    'result': 'success',
                    'msg': 'Success to delete the contact.'
                }
            else:
                to_return = {
                    'result': 'fail',
                    'msg': '要删除的联系人不存在！'
                }
        elif status == 'add':
            if last_data:
                to_return = {
                    'result': 'fail',
                    'msg': '联系人已存在！'
                }
            else:
                PhoneNumber.objects.create(
                    user_id=data.get('user_id'),
                    info_id=data.get('info_id'),
                    name=data.get('name'),
                    phone=data.get('phone')
                )
                to_return = {
                    'result': 'success',
                    'msg': 'Success to add the contact.'
                }
        elif status == 'change':
            # 多客户端修改同一条目冲突,这里比较标准的处理办法是给每次数据同步加上版本号,但是我没有采用
            # 我的处理办法是如果最新的数据和本地修改前的数据相同则同步数据,否则由用户选择要保留的数据
            if last_data and last_data[0].name == old_data.get('name') and last_data[0].phone == old_data.get('phone'):
                PhoneNumber.objects.filter(
                    user_id=data.get('user_id'),
                    info_id=data.get('info_id')
                ).update(
                    name=data.get('name'),
                    phone=data.get('phone')
                )
                to_return = {
                    'result': 'success',
                    'msg': 'Success to update the contact.'
                }
            else:
                # 用户选择要保留的数据
                # 选择保留修改则:前端更新old_data为这里返回的last_data，然后重新访问该api
                # 选择不保留修改则:前端将这里返回的last_data同步到用户端
                if last_data:
                    to_return = {
                        'result': 'choice',
                        'msg': u'本地数据不是最新，保留本次修改？',
                        'data': data,
                        'last_data': {
                            'name': last_data[0].name,
                            'phone': last_data[0].phone
                        }
                    }
                else:
                    to_return = {
                        'result': 'fail',
                        'msg': u'修改的联系人不存在！'
                    }
        if to_return['result'] == 'success':
            # 去掉发信的设备的信道，避免多余发送
            Group('mail-%s' % data.get('user_id')).discard(message.reply_channel)
            # 发送同步的数据
            Group('mail-%s' % data.get('user_id'), channel_layer=message.channel_layer).send({'text': message['text']})
            # 重新加入对应设备的信道
            Group('mail-%s' % data.get('user_id')).add(message.reply_channel)
        else:
            message.reply_channel.send({'text': json.dumps(to_return)})

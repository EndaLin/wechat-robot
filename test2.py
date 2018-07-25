import itchat
import requests
import time
import hashlib
import base64
from Crypto.Cipher import AES

KEY = 'ddcf14468ecc42c3859f073b68c16133'
SECRET = '1dba9552db45c48a'
Time = str(round(time.time() * 1000))

# def add_to_16(text):
#     print(text)
#     while len(text) % 16 != 0:
#         text += '\0'
#     return str.encode(text)  # 返回bytes
#
# #key是密码， text是待加密的文本
# def aes(key, text):
#     aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
#     encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')  # 加密
#     return encrypted_text
#
# #对数据进行MD5加密
# def md5(mess):
#     m = hashlib.md5()
#     m.update(mess.encode('utf-8'))
#     return m.hexdigest()
#
# def create_data(msg):
#     keyParam = SECRET + Time + KEY
#     aesKey = md5(keyParam)
#     data = aes(aesKey, str(msg))
#     return data


def get_response(msg):
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot'
    }
    Url = 'http://www.tuling123.com/openapi/api'
    rep = requests.post(Url, data)
    rep.encoding = 'utf-8'
    try:
        reps = rep.json().get('text')
        re_url = rep.json().get('url')
        re_lists = rep.json().get('lists')
        """ 当json中没有'url','lists'时，get方法返回None,"""
        if not re_url and not re_lists:
            return reps
        elif not re_lists:
            return reps+'\n'+re_url
        elif not re_url:
            return reps +'\n'+ re_lists
    except:
        return

# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    # defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.run()

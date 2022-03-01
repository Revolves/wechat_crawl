import imp
import time
import requests
from wechatarticles.utils import get_history_urls, timestamp2date

# 获取微信公众号__biz
def get_biz(name):
    """
    
    :param name:微信公众号名字
    
    :return :对应biz
    """
    quryUrl = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=0&sourceid=sugg&sut=0&sst0=1645702699879&lkt=0%2C0%2C0&p=40040108'.format(name)
    
name_to_biz = {
    '军武次位面':'MzI2MTA4Njg3Ng==',
    '空军之翼':"MzA3MTIzMjk2OQ==",
    '北国防务':'MzI1NjA2OTI2Mg==',
    '雷曼军事现代舰船':'MzA5MjI3NzgxMg==',
    '崎峻战史':'MzAwNzk3NDU2MA==',
    '讲武堂':'MjM5ODMzNTA0OA==',
    '军报记者':'MjM5MTE2NDUwMA==',
    '人民武警':'MzIyMDEwMTYwNQ==',
    '环球军事':'MzU2ODA0MjA0Ng==',
    '蒋校长':'MzIzNDYzODAyOA==',
    '米尔观天下':'MzA4NTkxOTc5Ng=='
}
print(timestamp2date(time.time()))

uin = 'MTcwNjE5MjgwMA=='
key = 'c4ef5b2c70f095b662e2a6226a1f96ef591de8103ba7414908c3d485380f1c126b66e745d690a80945d207143a3f45e26067e6dbdd0a5b16515d4e8e73d1039ea01bc82b0527b3180e15ec41617e06265b295d49ac71182b17d34fe4707b515cee5b6adc879dbe1cd15d9fb60c70e604a30c4b8183347274b5948af6e98b0591'
lst = get_history_urls('MzI2MTA4Njg3Ng==',uin=uin, key=key,)
print(lst)
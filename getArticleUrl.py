import requests

# 获取微信公众号__biz
def get_biz(name):
    """
    
    :param name:微信公众号名字
    
    :return :对应biz
    """
    quryUrl = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=0&sourceid=sugg&sut=0&sst0=1645702699879&lkt=0%2C0%2C0&p=40040108'.format(name)
    
name_to_biz = {
    '军武次位面':'',
    '空军之翼':"MzA3MTIzMjk2OQ==",
    '北国防务',
    '雷曼军事现代舰船',
    '崎峻战史',
    '讲武堂',
    '军报记者',
    '人民武警',
    '环球军事',
    '蒋校长',
    '米尔观天下'
}
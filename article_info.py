import os
from pprint import pprint
from wechatarticles import ArticlesInfo

if __name__ == "__main__":
    # 登录微信PC端获取文章信息
    appmsg_token, cookie = "appmsg_token", "cookie"
    article_url = "http://mp.weixin.qq.com/s?__biz=MzI2MTA4Njg3Ng==&mid=2652415663&idx=8&sn=786c45e5fba7925a95f31253737756d1&chksm=f1b3cd5cc6c4444aa3301451b85e545010932af1615eae2b4e25e77252bc39a06db722634a16#rd"
    test = ArticlesInfo(appmsg_token, cookie)
    comments = test.comments(article_url)
    read_num, like_num, old_like_num = test.read_like_nums(article_url)
    print("read_like_num:", read_num, like_num, old_like_num)
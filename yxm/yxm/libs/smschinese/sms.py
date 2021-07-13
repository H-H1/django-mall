import requests

def SMSC(mobiel,smstext):
    """GET短信 超简洁通道,六星python学院提供,KEY请勿传播!"""
    url = "http://utf8.api.smschinese.cn/?Uid=szxincd&Key=6d250b4cc2fdf01e2592&smsMob=" + mobiel + "&smsText=验证码:" + smstext
    r = requests.get(url)
    return r.content.decode()

if __name__ == '__main__':
    SMSC('18006511089','1234')
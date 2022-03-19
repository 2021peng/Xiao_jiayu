# 开发人：peng
# 开发时间 ：2022/3/19 20:16
import requests,json
while True:
    msg = input("我：")
    key = {
            #"key":"--这里输入你图灵机器人的APIKey--",
            "key":"******",
            "info":msg
           }
    url = "http://www.tuling123.com/openapi/api"
    request = requests.post(url,data=key)
    js = json.loads(request.text)
    print("Robot："+js["text"])

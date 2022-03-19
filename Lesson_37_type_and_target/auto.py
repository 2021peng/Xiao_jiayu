# 开发人：peng
# 开发时间 ：2022/3/19 18:25


def fishC_SignIn(Cookies):
    "参数Cookies，值：鱼C账号的Cookies。\n以Windows 10 64位的UA，合适的Referer以及你的账号的Cookies为请求头，\n向鱼C签到页面发起请求获取签到链接，然后向签到链接发起请求。"
    from urllib.request import Request,urlopen
    url='https://fishc.com.cn/plugin.php?id=k_misign:sign'
    cookies=Cookies if Cookies != '' else None
    if cookies==None:
        print('您未输入Cookies！')
        return False
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Referer':'https://fishc.com.cn/','Cookie':cookies}
    req=Request(url=url,headers=headers)
    print('正在请求签到链接……')
    html=urlopen(req).read().decode('gbk')
    print('服务器已响应，正在查找签到链接……\n')
    a=html.find('<a id="JD_sign" href="')+22 if html.find('<a id="JD_sign" href="')>-1 else -1
    b=html.find('" onclick=',a)
    rootUrl=html[a:b]
    if rootUrl=='':
        print('找不到签到链接，可能已经签过到了，也可能是账号的Cookies错误！')
    else:
        print('已找到签到链接，正在发出签到请求，请稍等……')
        url='https://fishc.com.cn/'+rootUrl
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Referer':'https://fishc.com.cn/plugin.php?id=k_misign:sign','Cookie':cookies}
        req=Request(url=url,headers=headers)
        urlopen(req)
        print('签到完成！')

if __name__=='__main__':
    print(fishC_SignIn.__doc__,'\n')
    fishC_SignIn(input('请输入你的鱼C账号的Cookies：'))
    #致小白：若要实现定时自动签到，
    #直接把上面的“input(...)”改成你的鱼C账号的cookies即可。


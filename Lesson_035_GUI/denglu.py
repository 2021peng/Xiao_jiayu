# 开发人：peng
# 开发时间 ：2022/3/17 15:15

"""
实现一个用于登记用户账号信息的界面
（如果是带 * 号的必填项，要求一定要有输入并且不能是空格）。
"""

import easygui as g

msg = "请填写以下联系方式"
title = "账号中心"
fieldNames = ["*用户名","*真实姓名","手机号码","QQ","*E-mail"]
fieldValues = []
fieldValues = g.multenterbox(msg,title,fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ('[%s]为必填项。\n\n'%fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)

print("用户资料如下：%s"%str(fieldValues))
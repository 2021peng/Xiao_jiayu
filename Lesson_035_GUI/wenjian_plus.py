# 开发人：peng
# 开发时间 ：2022/3/17 16:19

"""
在上一题的基础上增强功能：
当用户点击“OK”按钮的时候，比较当前文件是否修改过，如果修改过，
则提示“覆盖保存”、”放弃保存”或“另存为…”并实现相应的功能。
"""

import os
import easygui as g

file_path = g.fileopenbox(default="*.txt")

with open(file_path,encoding='utf-8') as old_file:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下："%title
    text = old_file.read()
    text_after = g.textbox(msg,title,text)

if text != text_after:
    #textbox的返回值会追加一个换行符
    choice = g.buttonbox("检测到文件的内容发生变化，请选择以下操作：","警告",("覆盖保存","放弃保存","另存为"))
    if choice == "覆盖保存":
        with open(file_path,'w+',encoding='utf-8') as old_file:
            old_file.write(text_after)
    if choice == "放弃":
        pass
    if choice == "另存为":
        another_path = g.filesavebox(default=".txt")
        if os.path.splitext(another_path)[1] != '.txt':
            another_path += '.txt'
        with open(another_path,'w+',encoding='utf-8') as new_file:
            new_file.write(text_after)


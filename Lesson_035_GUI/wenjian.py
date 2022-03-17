# 开发人：peng
# 开发时间 ：2022/3/17 16:05

import os
import easygui as g

file_path = g.fileopenbox(default="*.txt")

with open(file_path,encoding='utf-8') as f:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下："%title
    text = f.read()
    g.textbox(msg,title,text)

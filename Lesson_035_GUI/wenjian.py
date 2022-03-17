# 开发人：peng
# 开发时间 ：2022/3/17 16:05

"""
提供一个文件夹浏览框，让用户选择需要打开的文本文件，打开并显示文件内容。
"""

import os
import easygui as g

file_path = g.fileopenbox(default="*.txt")

with open(file_path,encoding='utf-8') as f:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下："%title
    text = f.read()
    g.textbox(msg,title,text)

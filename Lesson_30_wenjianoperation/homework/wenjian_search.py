# 开发人：peng
# 开发时间 ：2022/3/18 23:00
"""
编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。
如遇到文件夹，则进入文件夹继续搜索，
"""
import os
flags = 0

def search_file(start_file,target):
    os.chdir(start_file)    #切换到当前做目录
    global flags
    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file) #使用os.sep是程序更标准
            flags = 1
            break
        if os.path.isdir(each_file):
            search_file(each_file,target)   # 递归调用
            os.chdir(os.pardir)
        else:
            break

start_dir = input('请输入待查找的初始目录：')
target = input('请输入要查找的文件：')
search_file(start_dir,target)
if flags == 0:
    print('%s文件未在此目录！' % target)


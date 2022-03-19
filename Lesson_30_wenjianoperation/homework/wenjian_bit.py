# 开发人：peng
# 开发时间 ：2022/3/18 22:52
"""
编写一个程序，计算当前文件夹下所有文件的大小，
"""
import os
def file_size():
    file_name = os.listdir(os.curdir)
    dict1 = dict()

    for each_file in file_name:
        if os.path.isfile(each_file):
            dict1.setdefault(each_file,os.path.getsize(each_file))
            print('%s的大小为：【%d Bytes】'%(each_file,dict1[each_file]))

file_size()
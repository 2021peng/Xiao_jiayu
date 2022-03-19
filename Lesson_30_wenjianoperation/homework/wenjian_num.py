# 开发人：peng
# 开发时间 ：2022/3/18 21:07
"""
编写一个程序，统计当前目录下每个文件类型的文件数
"""
import os

file_path = input('请输入要查询的文件目录：')
#all_files = os.listdir(os.curdir)   # 使用os.curdir表示当前目录更标准
all_files = os.listdir(file_path)
#无法查看文件夹
type_dict = dict()  # 先定义一个字典，用来存放{’后缀名‘：数量}

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹',0)   # 当原字典当中没有该键时，则新增该键和对应的值，并且返回键值
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]    # 返回的值是元组，获取文件的后缀名=ext
        type_dict.setdefault(ext,0)
        type_dict[ext] += 1

for each_file in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件%d个'%(each_file,type_dict[each_file]))

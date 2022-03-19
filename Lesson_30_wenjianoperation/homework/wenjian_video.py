# 开发人：peng
# 开发时间 ：2022/3/19 11:34
"""

"""

import os


def search_file(start_dir, target):
    print(os.getcwd()+ '\nloop1')
    os.chdir(start_dir)
    path = os.getcwd()
    print(os.getcwd() + '\nloop2')
    list = os.walk(path)
    for each_file in list:
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep是程序更标准
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()
print(start_dir + '\ttest1')
print(program_dir + '\ttest2')

target = ['.mp4', '.avi', '.txt','.pdf','.rmvb']
vedio_list = []

search_file(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()


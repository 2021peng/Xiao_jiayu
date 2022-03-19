# 开发人：peng
# 开发时间 ：2022/3/19 11:34
"""
编写一个程序，用户输入开始搜索的路径，
查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4 rmvb, avi的格式即可），
并把创建一个文件（vedioList.txt）存放所有找到的文件的路径
"""
import os

ext_lis = []
def search_file(start_dir, target):
    #print(os.getcwd()+ '\nloop1')
    os.chdir(start_dir)
    #print(os.getcwd() + '\nloop2')

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        ext_lis.append(ext)
        if ext in target:
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep是程序更标准
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录


start_dir = input('请输入待查找的初始目录【如：C:/Users/admin/】：')
program_dir = os.getcwd()

target = ['.mp4', '.avi','.py','.rmvb']
vedio_list = []

search_file(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()
print(ext_lis)


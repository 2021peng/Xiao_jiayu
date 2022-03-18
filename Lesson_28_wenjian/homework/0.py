# 开发人：peng
# 开发时间 ：2022/3/17 20:41
"""
编写一个程序，接受用户的输入并保存为新的文件
"""
def file_write(file_name):
    f = open(file_name,'a+',encoding='utf-8')
    print("请输入内容【按’:w‘保存退出！】:")
    while True:
        a = input()
        if a != ':w':
            f.write('%s\n'%a)
        else:
            break
    f.close()

file_name = input("请输入要新建的文件名：")
file_write(file_name)
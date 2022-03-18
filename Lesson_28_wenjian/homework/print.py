# 开发人：peng
# 开发时间 ：2022/3/18 11:04
"""
编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上，
"""
def file_print(file_name,line_num):
    f = open(file_name,encoding='utf-8')
    print('\n文件%s的前%s行的内容如下：'%(file_name,line_num))
    for i in range(int(line_num)):
        print(f.readline(),end='')
    f.close()

#file_name = input("请输入要打开的文件名：")
file_name = input('请输入要打开的文件名(C:\\文件名.txt)：')
line_num = input("请输入需要显示该文件的前几行：")
file_print(file_name,line_num)


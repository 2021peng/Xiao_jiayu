# 开发人：peng
# 开发时间 ：2022/3/18 11:15
"""
要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。
如输入13:21打印第13行到第21行，输入:21打印前21行，
输入21:则打印从第21行开始到文件结尾所有内容
"""
def file_print(file_name,paragraph):
    (start,end) = paragraph.split(':')
    if start == '':
        start=1
    else:
        start = int(start)
    if end == '':
        end = -1
    else:
        end = int(end)
    f = open(file_name,encoding='utf-8')
    if start == 1:
        if end == -1:
            print("文件%s的从开头到结束的内容如下："%file_name)
        else:
            print("文件%s的从开头到%d行的内容如下："%(file_name,end))
    else:
        if end == -1:
            print("文件%s的从%d行到结束的内容如下：" % (file_name,start))
        else:
            print("文件%s的从%d行到%d行的内容如下：" % (file_name,start,end))
    for i in range(start-1):
        f.readline()
    num = end-start+1
    if num < 0:
        print(f.read())
    else:
        for i in range(num):
            print(f.readline())
    f.close()

file_name = input("请输入需要打开的文件(C:\\文件名.txt)：")
paragraph = input('请输入需要显示的行数【格式如 13：21 或 ：21 或 21： 】：')
while paragraph == '':
    paragraph = input('输入有误，请重新输入：')
file_print(file_name,paragraph)

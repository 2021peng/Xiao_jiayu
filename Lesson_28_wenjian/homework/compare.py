# 开发人：peng
# 开发时间 ：2022/3/17 20:58
"""
编写一个程序，比较用户输入的两个文件，如果不同，
显示出所有不同处的行号与第一个不同字符的位置，
"""
def file_compare(file1, file2):
    f1 = open(file1,encoding='utf-8')
    f2 = open(file2,encoding='utf-8')
    count = 0  # 统计行数
    differ = []  # 统计不一样的数量
    for line1 in f1:
        line2 = f2.readline() #一行一行的读取，自动读取下一行
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ


file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')

differ = file_compare(file1, file2)

if len(differ) == 0:
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：' % len(differ))
    print(differ)
    for each in differ:
        print('第%d行不一样' % each)
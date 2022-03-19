# 开发人：peng
# 开发时间 ：2022/3/19 14:40
"""
编写一个程序，这次要求使用pickle将文件（record.txt）里的对话按照以下要求腌制成不同文件
（没错，是第29讲的内容小改，考考你自己能写出来吗？）：
小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
文件中总共有三段对话，分别保存为
boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件
是以二进制保存的，所以打开会有乱码!
（提示：文件中不同的对话间已经使用“==========”分割）
"""
import pickle

def save_files(boy,girl,count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy,'wb')  # b,以二进制模式打开文件
    girl_file = open(file_name_girl,'wb')  # b,以二进制模式打开文件

    pickle.dump(boy,boy_file)
    pickle.dump(girl,girl_file)


def split_file(file_name):
    count = 1
    boy = []
    girl = []

    f = open(file_name,encoding='utf-8')
    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split(':',1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_files(boy,girl,count)

            count += 1
            boy = []
            girl = []

    save_files(boy,girl, count)
    f.close()

split_file('record.txt')
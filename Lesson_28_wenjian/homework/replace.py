# 开发人：peng
# 开发时间 ：2022/3/18 11:50

def file_replace(file_name,rep_word,new_word):
    f_read = open(file_name,encoding='utf-8')

    content = []
    count = 0

    for each_line in f_read:
        if rep_word in each_line:
            count += each_line.count(rep_word)
            each_line = each_line.replace(rep_word,new_word)
        content.append(each_line)

    decide = input('文件%s中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\nYES/NO:'
                   %(file_name,count,rep_word,rep_word,new_word))

    if decide in ['YES','Yes','yes']:
        f_write = open(file_name,'w',encoding='utf-8')
        f_write.writelines(content)
        f_write.close()
    f_read.close()

file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)


# 开发人：peng
# 开发时间 ：2022/3/17 14:54
import random
import easygui as g

g.msgbox("嗨，欢迎第一次使用！")
secret = random.randint(1,10)

msg = "猜一猜我心里想的是什么数字？"
title = "数字小游戏"
guess = g.integerbox(msg,title,lowerbound=5,upperbound=10,image='welcome.gif')

while True:
    if guess==secret:
        g.msgbox("恭喜你，猜中了！")
        break
    else:
        if guess>secret:
            g.msgbox("你猜大了~~~")
        else:
            g.msgbox("你猜小了~~~")
        guess = g.integerbox(msg,title,lowerbound=1,upperbound=10,image='welcome.gif')

g.msgbox("游戏结束！下次再来")
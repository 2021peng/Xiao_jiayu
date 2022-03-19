# 开发人：peng
# 开发时间 ：2022/3/19 16:58
"""
按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
    平日票价100元
    周末票价为平日的120%
    儿童半票
"""

class Ticket():
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self, num):
        return self.exp * self.inc * self.discount * num

adult = Ticket()
child = Ticket(child=True)
print("2个成人 + 3个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(3)))


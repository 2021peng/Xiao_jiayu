[easygui文档](http://www.javashuo.com/article/p-hraxvhdw-mg.html)



[TOC]

------

*因为版本更迭，本篇全部示例及截图均已更新，最新演示版本为 EasyGUI 0.98 & Python 3.7。*

*注意：因为模块、Python 版本或系统环境的差别，书中涉及的演示截图与实际环境可能会有出入，但函数的用法及行为均是一致。*

## **0. 安装 EasyGUI**

easygui官网：[http://easygui.sourceforge.net/](http://www.javashuo.com/link?url=http://easygui.sourceforge.net/)

github官网：[https://github.com/robertlugg/easygui](http://www.javashuo.com/link?url=https://github.com/robertlugg/easygui)

**使用 pip 进行安装：**

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/522_587_1c5.jpg) 
 

## **1. 什么是 EasyGUI？**

EasyGUI 是 Python 中一个很是简单的 GUI 编程模块，不一样于其余的 GUI 生成器，它不是事件驱动的。相反，全部的 GUI 交互都是经过简地函数调用就能够实现。

EasyGUI 为用户提供了简单的 GUI 交互接口，不须要程序员知道任何有关 tkinter，框架，部件，回调或 lambda 的任何细节。

EasyGUI 能够很好地兼容 Python 2 和 3，而且不存在任何依赖关系。

EasyGUI 是运行在 Tkinter 上并拥有自身的事件循环，而 IDLE 也是 Tkinter 写的一个应用程序并也拥有自身的事件循环。所以当二者同时运行的时候，有可能会发生冲突，且带来不可预测的结果。所以若是你发现你的 EasyGUI 程序有这样的问题，请尝试在 IDLE 外去运行你的程序。

## **2. 一个简单的例子**

在 EasyGui 中，全部的 GUI 互动均是经过简单的函数调用，下边一个简单的例子告诉你 EasyGui 确实很 Easy！

```python
import easygui as g
import sys

while 1:
        g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")

        msg ="请问你但愿在鱼C工做室学习到什么知识呢？"
        title = "小游戏互动"
        choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
        
        choice = g.choicebox(msg, title, choices)

        # 注意，msgbox的参数是一个字符串
        # 若是用户选择Cancel，该函数返回None
        g.msgbox("你的选择是: " + str(choice), "结果")

        msg = "你但愿从新开始小游戏吗？"
        title = "请选择"

        # 弹出一个Continue/Cancel对话框
        if g.ccbox(msg, title):
                pass            # 若是用户选择Continue
        else:
                sys.exit(0)     # 若是用户选择Cancel
```

## **3. EasyGUI 的各类功能演示**

要运行 EasyGUI 的演示程序，在命令行调用 EasyGUI 是这样的：
 

```python
python easygui.py
```

或者能够从 IDE（例如 IDLE, PythonWin, Wing, 等等）上调用：
 

```python
>>> import easygui
>>> easygui.egdemo()
```


成功调用后将能够尝试 EasyGUI 拥有的各类功能，并将结果打印至控制台。

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/523_24b_66c.png)

## **4. 导入 EasyGUI**

为了使用 EasyGUI 这个模块，你应该先导入它。

最简单的导入语句是：

```
import easygui
```

若是使用上面这种形式导入的话，那么你使用 EasyGUI 的函数的时候，必须在函数的前面加上前缀 easygui，像这样：

```
easygui.msgbox(...)
```

另外一种选择是导入整个 EasyGUI 包：

```
from easygui import *
```

这使得咱们更容易调用 EasyGUI 的函数，能够直接这样编写代码：

```
msgbox(...)
```

第三种方案是使用相似下边的 import 语句：

```
import easygui as g
```

这种方法还可让你保持 EasyGUI 的命名空间，同时减小你的打字数量。

导入以后就能够这么调用 EasyGUI 的函数：

```
g.msgbox(...)
```

## **5. 使用 EasyGUI**

一旦你的模块导入 EasyGUI，GUI 操做就是一个简单的调用 EasyGUI 函数的几个参数的问题了。

例如，使用 EasyGUI 来实现世界上最著名的打招呼：

```
import easygui as g

g.msgbox("Hello, world!")
```


![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/524_666_4ff.png)

## **6. EasyGUI 函数的默认参数**

对于全部对话框而言，前两个参数都是消息主体和对话框标题。

按照这个规律，在某种状况下，这可能不是理想的布局设计（好比当对话框在获取目录或文件名的时候会选择忽略消息参数），但保持这种一致性且贯穿于全部的窗口部件是更为得体的考虑！
   
绝大部分的 EasyGUI 函数都有默认参数，几乎全部的组件都会显示消息主体和对话框标题。

标题默认是空字符串，消息主体一般有一个简单的默认值。
  
这使得你能够尽量少的去设置参数，好比 msgbox() 函数标题部分的参数是可选的，所以你调用 msgbox() 的时候只须要指定一个消息参数便可，例如：

```
>>> msgbox('我爱小甲鱼^_^')
```

固然你也能够指定标题参数和消息参数，例如：

```
>>> msgbox('我爱小甲鱼^_^', '鱼油心声')
```


![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/525_322_d76.png) 

在各种按钮组件里，默认的消息是 “Shall I continue?”，因此你能够不带任何参数地去调用它们。

这里咱们演示不带任何参数地去调用 ccbox()，当选择 “cancel” 或关闭窗口的时候返回一个布尔类型的值：

```
if ccbox(): 
        pass         # 用户选择继续
else: 
        return      # 用户选择取消
```

## **7. 使用关键字参数调用 EasyGUI 的函数**

调用 EasyGUI 函数还可使用关键字参数哦。

如今假设你须要使用一个按钮组件，但你不想指定标题参数（第二个参数），你仍可使用关键字参数的方法指定 choices 参数（第三个参数），像这样：

```
>>> choices = ['愿意', '不肯意', '有钱的时候就愿意']
>>> reply = choicebox('你愿意购买资源打包支持小甲鱼吗？', choices = choices)
```


![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/526_4d7_130.png)

## **8. 使用按钮组件**

根据需求，EasyGUI 在 buttonbox() 上创建了一系列的函数供调用。

**8.1 msgbox()**

*msgbox(msg='(Your message goes here)', title=' ', ok_button='OK', image=None, root=None)*

msgbox() 显示一个消息和提供一个 “OK” 按钮，你能够指定任意的消息和标题，你甚至能够重写 “OK” 按钮的内容。

重写 “OK” 按钮最简单的方法是使用关键字参数：

```
>>> msgbox("我必定要学会编程!", ok_button="加油!")
```


![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/527_d18_808.png)

**8.2 ccbox()**

*ccbox(msg='Shall I continue?', title=' ', choices=('C[o]ntinue', 'C[a]ncel'), image=None, default_choice='C[o]ntinue', cancel_choice='C[a]ncel')*

ccbox() 提供一个选择：“C[o]ntinue” 或者 “C[a]ncel”，并相应的返回 True 或者 False。

注意：“C[o]ntinue” 中的 [o] 表示快捷键，也就是说当用户在键盘上敲一下 o 字符，就至关于点击了 “C[o]ntinue” 按键。

**8.3 ynbox()**

*ynbox(msg='Shall I continue?', title=' ', choices=('[<F1>]Yes', '[<F2>]No'), image=None, default_choice='[<F1>]Yes', cancel_choice='[<F2>]No')*

跟 ccbox() 同样，只不过这里默认的 choices 参数值不一样而已，[<F1>] 表示将键盘上的 F1 功能按键做为 “Yes” 的快捷键使用。

***8.4 buttonbox()***

*buttonbox(msg='', title=' ', choices=('Button[1]', 'Button[2]', 'Button[3]'), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True)*

可使用 buttonbox() 定义本身的一组按钮，buttonbox() 会显示一组由你自定义的按钮。

当用户点击任意一个按钮的时候，buttonbox() 返回按钮的文本内容。

若是用户点击取消或者关闭窗口，那么会返回默认选项（第一个选项）。

请看例子：

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/528_8f6_c5e.png) 


***8.5 indexbox()***

*indexbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None, default_choice='Yes', cancel_choice='No')*

基本跟 buttonbox() 同样，区别就是当用户选择第一个按钮的时候返回序号 0， 选择第二个按钮的时候返回序号 1。


**8.6 boolbox()**

*boolbox(msg='Shall I continue?', title=' ', choices=('[Y]es', '[N]o'), image=None, default_choice='Yes', cancel_choice='No')*

若是第一个按钮被选中则返回 True，不然返回 False。

## **9. 如何在 buttonbox 里边显示图片**

当你调用一个 buttonbox 函数（例如 msgbox(), ynbox(), indexbox() 等等）的时候，你还能够为关键字参数 image 赋值，能够设置一个 .gif 格式的图像（PNG 格式的图像也是支持的哦^_^）：

```
buttonbox('你们说我长得帅吗？', image='turtle.gif', choices=('帅', '不帅', '!@#$%'))
```


![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/529_a60_54d.png)

## **10. 为用户提供一系列选项**

**10.1 choicebox()**

*choicebox(msg='Pick an item', title='', choices=[], preselect=0, callback=None, run=True)*

按钮组件方便提供用户一个简单的按钮选项，但若是有不少选项，或者选项的内容特别长的话，更好的策略是为它们提供一个可选择的列表。   
   
choicebox() 为用户提供了一个可选择的列表，使用序列（元祖或列表）做为选项，这些选项会按照字母进行排序。

另外还可使用键盘来选择其中一个选项（比较纠结，但一点儿都不重要）：
 

- 例如当按下键盘上的 “g” 键，将会选中的第一个以 “g” 开头的选项。再次按下 “g” 键，则会选中下一个以 “g” 开头的选项。在选中最后一个以 “g” 开头的选项的时候，再次按下 “g” 键将从新回到在列表的开头的第一个以 “g” 开头的选项。
- 若是选项中没有以 “g” 开头的，则会选中字符排序在 “g” 以前（“f”）的那个字符开头的选项
- 若是选项中没有字符的排序在 “g” 以前的，那么在列表中第一个元素将会被选中。


结合咱们以前学习的文件操做，举个高达上的例子（*源代码在第35讲的课后做业中^_^*）：

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/530_2a3_703.png) 

***10.2 multchoicebox()***

*multchoicebox(msg='Pick an item', title='', choices=[], preselect=0, callback=None, run=True)*

multchoicebox() 函数也是提供一个可选择的列表，与 choicebox() 不一样的是，multchoicebox() 支持用户选择 0 个，1 个或者同时选择多个选项。

multchoicebox() 函数也是使用序列（元祖或列表）做为选项，这些选项显示前会按照不区分大小写的方法排好序。

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/531_b1c_be0.png)

## **11. 让用户输入消息**

**11.1 enterbox()**

*enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)*

enterbox() 为用户提供一个最简单的输入框，返回值为用户输入的字符串。

默认返回的值会自动去除首尾的空格，若是须要保留首尾空格的话请设置参数 strip=False。

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/532_398_88d.png) 

**11.2 integerbox()**

*integerbox(msg='', title=' ', default=None, lowerbound=0, upperbound=99, image=None, root=None)*

integerbox() 为用户提供一个简单的输入框，用户只能输入范围内（lowerbound 参数设置最小值，upperbound 参数设置最大值）的整型数值，不然会要求用户从新输入。

**11.3 multenterbox()**

*multenterbox(msg='Fill in values for the fields.', title=' ', fields=[], values=[], callback=None, run=True)*

multenterbox() 为用户提供多个简单的输入框，要注意如下几点：
 

- 若是用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户为输入的选项。
- 若是用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。
- 若是用户取消操做，则返回域中的列表的值或者 None 值。


实现以下图（*源代码在第35讲的课后做业中^_^*）：

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/533_ddc_586.png)

## **12. 让用户输入密码**

有时候可能须要让用户输入密码等敏感信息，那么界面看上去应该是这样的：*******。

***12.1 passwordbox()***

*passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None)*

passwordbox() 跟 enterbox() 样式同样，不一样的是用户输入的内容用星号（*）显示出来，该函数返回用户输入的字符串：

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/534_e73_0d4.png) 


***12.2 multpasswordbox()***

*multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=(), callback=None, run=True)*

multpasswordbox() 跟 multenterbox() 使用相同的接口，但当它显示的时候，最后一个输入框显示为密码的形式（*）：

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/535_556_bfa.png)

## **13. 显示文本**

EasyGUI 还提供函数用于显示文本。

***13.1 textbox()***

*textbox(msg='', title=' ', text='', codebox=False, callback=None, run=True)*

textbox() 函数默认会以比例字体（参数 codebox=True 设置为等宽字体）来显示文本内容（自动换行），这个函数适合用于显示通常的书面文字。

注：text 参数设置可编辑文本区域的内容，能够是字符串、列表或者元祖类型。

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/536_545_cd0.png) 

***13.2 codebox()***

*codebox(msg='', title=' ', text='')*

codebox() 以等宽字体显示文本内容（不自动换行），至关于 textbox(codebox=True)

注：等宽字体很丑的，但适合代码编写，不信你试试看@_@

## **14. 目录与文件**

GUI 编程中一个常见的场景是要求用户输入目录及文件名，EasyGUI 提供了一些基本函数让用户来浏览文件系统，选择一个目录或文件。

***14.1 diropenbox()***

*diropenbox(msg=None, title=None, default=None)*

diropenbox() 函数用于提供一个对话框，返回用户选择的目录名（带完整路径哦），若是用户选择 “Cancel” 则返回 None。

default 参数用于设置默认的打开目录（请确保设置的目录已存在）。

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/537_fbb_90a.png) 

***14.2 fileopenbox()***

*fileopenbox(msg=None, title=None, default='\*', filetypes=None, multiple=False)*

fileopenbox() 函数用于提供一个对话框，返回用户选择的文件名（带完整路径哦），若是用户选择 “Cancel” 则返回 None。

关于 default 参数的设置方法：

- default 参数指定一个默认路径，一般包含一个或多个通配符。
- 若是设置了 default 参数，fileopenbox() 显示默认的文件路径和格式。
- default 默认的参数是 '*'，即匹配全部格式的文件。

例如：

- default="c:/fishc/*.py" 即显示 C:\fishc 文件夹下全部的 Python 文件。
- default="c:/fishc/test*.py" 即显示 C:\fishc 文件夹下全部的名字以 test 开头的 Python 文件。

关于 filetypes 参数的设置方法：

- 能够是包含文件掩码的字符串列表，例如：filetypes = ["*.txt"]
- 能够是字符串列表，列表的最后一项字符串是文件类型的描述，例如：filetypes = ["*.css", ["*.htm", "*.html", "HTML files"]]

最后是 multiple 参数，若是为 True 则表示能够同时选择多个文件。

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/538_c81_169.png) 

***14.3 filesavebox()***

*filesavebox(msg=None, title=None, default='', filetypes=None)*

filesavebox() 函数提供一个对话框，让用于选择文件须要保存的路径（带完整路径哦），若是用户选择 “Cancel” 则返回 None。

default 参数应该包含一个文件名（例如当前须要保存的文件名），固然也能够设置为空的，或者包含一个文件格式掩码的通配符。

filetypes 参数的设置方法请参考 fileopenbox() 函数。

![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/539_e4d_8ae.png)

## **15. 记住用户的设置**

***15.1 EgStore***

GUI 编程中一个常见的场景就是要求用户设置一下参数，而后保存下来，以便下次用户使用你的程序的时候能够记住他的设置。

为了实现对用户的设置进行存储和恢复这一过程，EasyGUI 提供了一个叫作 EgStore 的类。

为了记住某些设置，你的应用程序必须定义一个类（下面案例中的 “Settings”）继承自 EgStore 类。

而后你的应用程序必须建立一个该类的实例化对象（下面案例中的 “settings”）。

设置类的构造函数（__init__ 方法）必须初始化全部的你想要它所记住的那些值。

一旦你这样作了，你就能够在 settings 对象中经过设定值去实例化变量，从而很简单地记住设置。

以后使用 settings.store() 方法在硬盘上持久化保存。

下面建立一个叫作 “Settings” 的类：
 

```
from easygui import EgStore

# 定义一个叫作“Settings”的类，继承自EgStore类
class Settings(EgStore):

    def __init__(self, filename):  # 须要指定文件名
        # 指定要记住的属性名称
        self.author = ""
        self.book = ""

        # 必须执行下面两个语句
        self.filename = filename
        self.restore()

# 建立“Settings”的实例化对象“settings”
settingsFilename = "settings.txt"
settings = Settings(settingsFilename)

author = "小甲鱼"
book = "《零基础入门学习Pyhon》"

# 将上面两个变量的值保存到“settings”对象中
settings.author = author
settings.book = book
settings.store()
print("\n保存完毕\n")
```

## **16. 捕获异常**

***exceptionbox()***

使用 EasyGUI 编写 GUI 程序，有时候不免会产生异常。固然这取决于你如何运行你的应用程序，当你的应用程序崩溃的时候，堆栈追踪可能会被抛出，或者被写入到 stdout 标准输出函数中。

EasyGUI 经过 exceptionbox() 函数提供了更好的方式去处理异常。

当异常出现的时候，exceptionbox() 会将堆栈追踪显示在一个 codebox() 中，而且容许你作进一步的处理。

exceptionbox() 很容易使用，下面举个例子：

```
try:
        print('I Love FishC.com!')
        int('FISHC') # 这里会产生异常
except:
        exceptionbox()
```


![img](https://ewr1.vultrobjects.com/imgur2/000/004/466/540_8dd_2cd.png)
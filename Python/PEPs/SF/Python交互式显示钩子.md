# PEP 217 -- Python交互式显示钩子

|PEP编号:|217|
|:----|:----|
|标题:|Python交互式显示钩子|
|作者:|	moshez at zadka.site.co.il (Moshe Zadka)|
|状态:|Final|
|类型:|Standards Track|
|创建时间:|31-Jul-2000|
|Python版本:|2.1|
|上传历史|
---
内容

*   [摘要](#摘要)
*   [接口](#接口)
*   [解决方案](#解决方案)
*   [Jython解释器的问题](#Jython解释器的问题)


[摘要](#摘要)
=====================
Python中的信息交互式非常重要的--可以在代码中编写内容使其打印出来。但是，并不是每个人都想使用一样的打印方法，当打印方法不能满足需求的时候。本PEP提供了一种基于内置方法的解决防范。用户可以方便的改变打印函数。

[接口](#接口)
=====================
Python现有的解决方案满足了绝大多数的用户，所以不要改写它。在默认配置的情况下，交互式解释器的循环不会发生任何变化。想要更改解释的打印方法，用户需要将sys.displayhook重新绑定其他对象。使用交互式解释器调用这个对象的话，对象的结果是可以打印的，对象的内容会输出到sys.stdout上


[解决方案](#解决方案)
=====================
字节码 PRINT _EXPR 会调用 sys.displayhook(POP()), displayhook()会被添加到系统的内建函数中，等价于：
(译者，原文代码如此。简单来说，就是调用sys.displayhook(string)的话，等价于print(string);builtin._=string。其中builtin和__builtin__都是内建.py。名称不同是py2,py3的区别之一。)
```python
import __builtin__
def displayhook(o):
    if o is None:
        return
    __builtin__._ = None
    print `o`
    __builtin__._ = o
```


[Jython解释器的问题](#Jython解释器的问题)
=====================
Py.printResult 方法也会发生相类似的改变。





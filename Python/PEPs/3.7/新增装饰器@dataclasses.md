## PEP 557 Data Classes

|PEP编号:|557|
|:----|:----|
| 标题：     | Data Classes|
| 作者：      | Eric V. Smith <eric at trueblade.com>   |
| 状态 :       |    Final   |
| 类型：        |    Standards Track   |
| 创建时间：        |    2017-06-02   |
| Python版本：        |    3.7   |
| 上传历史：        | 2017-02-08, 2017-11-25, 2017-11-30, 2017-12-01, 2017-12-02, 2018-01-06, 2018-03-04 |
| 决议：        |    https://mail.python.org/pipermail/python-dev/2017-December/151034.html   |

内容
+ 审阅人员注意
+ 摘要
+ 原理
+ 规范
    + Field对象
    + post-init处理
    + 类变量
    + Init-only变量
    + Frozen实例
    + 继承
    + default_factory函数
    + 可变默认值
    + 模块级辅助函数
+ 讨论
    + python-ideas讨论
    + 支持自动设置__slots__?
    + 为什么不使用namedtuple?
    + 为什么不直接使用types . namedtuple呢?
    + 为什么不使用attrs？
    + post-init参数
    + asdict和astuple函数名
+ 被拒绝的想法
    + 在replace()中创建新对象后复制init=False字段
    + 自动支持可变的默认值
+ 例子
    + 自定义__init__方法
    + 一个复杂的例子
+ 致谢
+ 参考
+ 版权

### 读者注意
本PEP和初始实现是在一个单独的回购协议中起草的：https：//github.com/ericvsmith/dataclasses。在公开论坛发表评论之前，请至少阅读本PEP末尾列出的讨论。
    
### 摘要
本PEP描述了对标准库添加名为Data Classes的库，虽然Data Classes使用了一种非常不同的机制，但它们可以被认为是“具有默认值的可变命名元组”。因为Data Classes使用普通的类定义语法，所以可以自由地使用继承、元类、文档字符串、自定义方法、类工厂和其他Python类特性。

如PEP 526 “变量注释的语法”中所定义的那样，它提供了一个类装饰器，检查带有类型注释的变量的类定义。在本文档中，此类变量称为字段。使用这些字段，装饰器将生成的方法添加到类中，支持实例初始化,repr，比较方法以及“ 规范”部分中描述的可选的其他方法,这样的类被称为Data Classes,但该类没有什么特别之处：装饰器将生成的方法添加到类中并返回给定的类。

举个例子：

```python
@dataclass
class InventoryItem:
    '''用于跟踪库存中物品的等级。'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```
该@dataclass装饰将增加这些方法的InventoryItem类相当于：
```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0) -> None:
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
def __repr__(self):
    return f'InventoryItem(name={self.name!r}, unit_price={self.unit_price!r}, quantity_on_hand={self.quantity_on_hand!r})'
def __eq__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) == (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __ne__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) != (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __lt__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) < (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __le__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) <= (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __gt__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) > (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __ge__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) >= (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
```

Data Classes使您无需编写和维护这些方法。

### 原理
已经有许多尝试定义类，这些类主要用于存储可通过属性查找访问的值。一些例子包括:
+ 标准库中的collections.namedtuple。
+ 标准库中的typing.NamedTuple。
+ 热门的attrs [1]项目。
+ George Sakkis的recordType recipe [2]，一个受collections.namedtuple启发的可变数据类型。
+ 许多在线方法示例[3]，包[4]和问题[5]。David Beazley使用一种形式的数据类作为PyCon 2013元类谈话中的激励示例[6]。

那么，为什么需要这个PEP？

通过添加PEP 526，Python可以简洁地指定类成员的类型。此PEP利用该语法提供一种简单，不显眼的方式来描述Data Classes。除了两个例外，指定的属性类型批注被Data Classes完全忽略。

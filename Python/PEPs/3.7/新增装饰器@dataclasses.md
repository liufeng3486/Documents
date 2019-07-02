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

Data Classes不使用基类或元类。这些类的用户可以自由地使用继承和元类，而不受Data Classes的任何干扰。修饰后的类是真正的“普通”Python类。Data Classes装饰器不应该干扰类的任何使用。

Data Classes的一个主要设计目标是支持静态类型检查器。PEP 526语法的使用就是一个例子，但是fields（）函数和@dataclass装饰器的设计也是如此。由于它们的动态特性，上面提到的一些库很难与静态类型检查器一起使用。

Data Classes不是，也不是所有上述库的替换机制。但是，在标准库中，将允许许多更简单的用例改为利用Data Classes。列出的许多库具有不同的特性集，当然还会继续存在和发展。

哪里不适合使用Data Classes？
+ 需要与元组或字典兼容的API。
+ 除了PEPs 484和526提供的类型验证之外，还需要进行值验证或转换。

### 规范
本PEP中描述的所有功能都将存在于名为dataclasses的模块中 。

通常用作类装饰器的函数dataclass，被提供给后处理类并添加生成的方法，如下所述。

dataclass装饰器检查类查找字段。字段定义为__annotations__中标识的任何变量，也就是说，一个具有类型注释的变量。除了下面描述的两个例外，没有一个Data Classes机制检查注释中指定的类型。

请注意，__annotations__在类声明顺序中保证是有序映射。所有生成的方法中的字段顺序是它们在类中出现的顺序。

数据类装饰器将向类添加各种“dunder”方法，如下所述。如果类上已经存在任何添加的方法，则会引发一个TypeError。装饰器返回被调用的同一个类:不创建新类。

DataClass修饰符通常不带参数和括号。但是，它还支持以下逻辑签名：
```python
def dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
```
如果将DataClass用作不带参数的简单修饰器，则它的作用就像它具有记录在此签名中的默认值一样。也就是说，@dataclass的这三种用法是等效的：
```python
@dataclass
class C:
    ...

@dataclass()
class C:
    ...

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class C:
    ...
```

DataClass的参数是：
+ init: 如果为true（默认值），将生成__init__方法。
+ repr: 如果为true（默认值），将生成__repr__方法。

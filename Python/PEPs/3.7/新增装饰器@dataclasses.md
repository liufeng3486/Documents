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
+ repr: 如果为true（默认值），将生成__repr__方法。生成的repr字符串将包含类名以及每个字段的名称和repr，按照它们在类中定义的顺序排列。标记为被排除在repr之外的字段不包括在内。例如:InventoryItem(name='widget'， unit_price=3.0, quantity_on_hand=10)。
如果类已经定义了_repr__，则忽略该参数。

+ eq:如果为true(默认值)，将生成一个_eq__方法。按顺序，该方法将类作为其字段的元组进行比较。比较中的两个实例必须具有相同的类型。

如果类已经定义了_eq__，则忽略该参数。

+ order:如果为true(缺省值为False)，将生成__lt__、__le__、__gt__和__ge__方法。按照顺序，它们将类作为其字段的元组进行比较。比较中的两个实例必须具有相同的类型。如果order为真，eq为假，则会引发ValueError。

如果类已经定义了任何__lt__、__le__、__gt__或__ge__，则会引发ValueError。

+ unsafe_hash:如果为False(默认值)，则根据eq和frozen的设置方式生成_hash__方法。

如果eq和frozen都为true，数据类将为您生成一个__hash__方法。如果eq为真，frozen为假，那么将会将__hash__设置为None，标记为unhashable(确实如此)。如果eq为false，则将不使用__hash__，这意味着将使用超类的__hash__方法(如果超类是object，这意味着它将返回到基于id的散列)。

虽然不推荐，但是您可以强制 Data Classes创建一个带有unsafe_hash=True的__hash__方法。如果您的类在逻辑上是不可变的，但仍然可以进行修改，则可能会出现这种情况。这是一个特殊的用例，应该仔细考虑。

如果一个类已经有一个显式定义的__hash__，那么添加__hash__时的行为将被修改。显式定义的__hash__在以下情况下定义:
    + 类中定义了__eq__，并且用除None之外的任何值定义了__hash__。
    + 类中定义了__eq__，并且定义了任何非空的__hash__。
    + 类上没有定义__eq__，并且定义了任何__hash__。
    
如果unsafe_hash为真，并且显式定义了一个__hash__，则会引发ValueError。

如果unsafe_hash为false，并且显式定义了一个__hash__，则不添加任何__hash__。

有关更多信息，请参阅Python文档[7]。

+ frozen: 如果为真(默认为假)，分配给字段将生成异常。这模拟只读冻结实例。如果类中定义了_getattr__或_setattr__，则会引发ValueError。参见下面的讨论。

字段可以选择指定一个默认值，使用普通Python语法:
```python
@dataclass
class C:
    a: int       # 'a' has no default value
    b: int = 0   # assign a default value for 'b'
```
在本例中，a和b都包含在添加的__init__方法中，该方法定义为:
```python
def __init__(self, a: int, b: int = 0):
```
如果没有默认值的字段跟随具有默认值的字段，则会引发TypeError。无论是在单个类中发生这种情况，还是作为类继承的结果，都是如此。

对于普通和简单的用例，不需要其他功能。但是，有些 Data Class特性需要每个字段额外的信息。为了满足对附加信息的需求，可以使用对提供的field()函数的调用替换默认字段值。field()的签名为:
```python
def field(*, default=MISSING, default_factory=MISSING, repr=True,
          hash=None, init=True, compare=True, metadata=None)
```
缺失的值是一个sentinel对象，用于检测是否提供了默认值和default_factory参数。使用这个标记是因为None是默认值的有效值。

field()的参数为:
+ default:如果提供，这将是该字段的默认值。这是必需的，因为字段调用本身替换了默认值的正常位置。

+ default_factory:如果提供，那么它必须是一个零参数可调用的，当这个字段需要一个默认值时，它将被调用。在其他用途中，这可以用于指定具有可变默认值的字段，如下所述。同时指定default和default_factory错误的。

+ init:如果为true(默认值)，该字段将作为参数包含到生成的__init__方法中。

+ repr:如果为真(默认值)，则该字段包含在生成的__repr__方法返回的字符串中。

+ compare: 如果为True(默认值)，则生成的等式和比较方法(__eq__, __gt__, et al.)中包含该字段。

+ hash:这个可以是bool，也可以是None。如果为真，则该字段包含在生成的_hash__方法中。如果没有(默认值)，则使用compare的值:这通常是预期的行为。如果字段用于比较，则应该在散列中考虑它。不建议将此值设置为None以外的任何值。

设置hash=False而compare=True的一个可能原因是，如果计算一个字段的hash值很昂贵，那么这个字段就需要进行相等性测试，并且还有其他字段对类型的hash值有贡献。即使字段被排除在散列之外，它仍然用于比较。

+ metadata:可以是映射，也可以没有。None被视为空的dict。该值被包装在类型中。将其设置为只读，并在字段对象上公开。它根本不被Data Classes使用，而是作为第三方扩展机制提供的。多个第三方都可以拥有自己的密钥，以便在元数据中用作名称空间。

如果字段的默认值是通过调用field()指定的，那么这个字段的class属性将被指定的默认值替换。如果没有提供默认值，那么class属性将被删除。其目的是在dataclass装饰器运行后，类属性将包含字段的默认值，就像指定默认值本身一样。例如：
```python
@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20
```

类属性C.z是10，类属性C.t为20，类属性为C.x和C.y未设定。

### Field 对象
字段对象描述每个定义的字段。这些对象是在内部创建的，并由fields()模块级方法返回(参见下面)。用户永远不应该直接实例化字段对象。其文件化的属性是:
+ name:字段的名称。
+ 类型:字段的类型。
+ default、default_factory、init、repr、hash、compare和metadata具有与 field()声明中相同的含义和值。

其他属性可能存在，但它们是私有的，不能检查或依赖。

### post-init处理
生成的__init__代码将调用一个名为__post_init__的方法，如果它是在类上定义的。它将被称为self. __post_init__()。如果没有生成__init__方法，则不会自动调用__post_init__。

在其他用途中，这允许初始化依赖于一个或多个其他字段的字段值。例如:
```python
@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b
```

有关将参数传递给__post_init __（）的方法，请参阅下面有关init-only变量的部分。另请参阅有关replace（）如何处理init = False字段的警告 。

### 类变量
dataclass实际检查字段类型的一个地方是确定字段是否是PEP 526中定义的类变量。它通过检查字段的类型是否为type . classvar来实现这一点。如果一个字段是一个ClassVar，那么它将被排除在作为字段的考虑之外，并被 Data Class机制忽略。有关更多讨论，请参见[8]。函数不会返回这样的ClassVar伪字段。

### Init-only变量
dataclass检查类型注释的另一个地方是确定字段是否是只包含init的变量。它通过查看字段的类型是否是dataclass.initvar类型来实现这一点。如果一个字段是一个InitVar，那么它就被认为是一个伪字段，称为 init-only字段。因为它不是一个真正的字段，所以模块级fields()函数不会返回它。Init-only字段作为参数添加到生成的__init__方法中，并传递给可选的__post_init__方法。Data Classes不使用它们。

例如，假设一个字段将从数据库初始化，如果在创建类时没有提供值:
```python
@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(10, database=my_database)
```

# PEP 562 -- Python module级别的\_\_getattr\_\_和\_\_dir\_\_

|PEP编号:|562|
|:----|:----|
|标题:|Python module级别的\_\_getattr\_\_和\_\_dir\_\_|
|作者:|Ivan Levkivskyi <levkivskyi at gmail.com>|
|状态:|Final|
|类型:|Standards Track|
|创建时间:|09-Sep-2017|
|Python版本:|3.7|
|上传历史:|09-Sep-2017|
|决议:|https://mail.python.org/pipermail/python-dev/2017-December/151033.html|
---
内容

*   [摘要](#摘要)
*   [理论基础](理论基础)
*   [详述](#详述)
*   [向下兼容性及性能相关](#向下兼容性及性能相关)
*   [注意事项](#注意事项)
*   [参考文献](#参考文献)
*   [版权](#版权)

[摘要](#摘要)
=====================
建议支持\_\_getattr\_\_和\_\_dir\_\_在模块中的自定义，提供模块属性访问的基本定制功能。

[理论基础](#理论基础)
=====================
定制或者其他方式来控制对模块属性的访问，在某些情况下很方便。最典型的例子就是 管理弃用的警告。最典型的方案是，将模块的\_\_class__分配给types.ModuleType的自定义子类，或者使用自定义的装饰器实例替换sys.modules。通过直接在模块中定义\_\_getattr__可以很方便的实现这个功能。除了是被定义在模块中意外，它与普通的\_\_getattr__很像。例如：

# lib.py
```python

from warnings import warn

deprecated_names = ["old_function", ...]

def _deprecated_old_function(arg, other):
    ...

def __getattr__(name):
    if name in deprecated_names:
        warn(f"{name} is deprecated", DeprecationWarning)
        return globals()[f"_deprecated_{name}"]
    raise AttributeError(f"module {__name__} has no attribute {name}")
```
# main.py
```python
from lib import old_function  # 可以运行，但是会报警
```

\_\_getattr__的另一个比较常用的场景就是 惰性导入子模块(懒加载)。一个简单的例子:
（译者：以下例子做的事情是。在main.py里调用lib.submod时，由于并没有加载相关内容，会运行lib/\_\_init__.py中的\_\_getattr__方法，在\_\_getattr__中判断是\_\_all__中是否存在相关内容，再加载。以达到懒加载的目的）
# lib/\_\_init__.py
```python
import importlib

__all__ = ['submod', ...]

def __getattr__(name):
    if name in __all__:
        return importlib.import_module("." + name, __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
```
# lib/submod.py
```python
print("Submodule loaded")
class HeavyClass:
    ...
```
# main.py
```python
import lib
lib.submod.HeavyClass  # prints "Submodule loaded"
```
PEP549提出了使用实例属性的方式来完成相类似的功能。不同的是，本PEP的实现方式更加快捷、更加简单，而且提供了更多更基础的可定制化选项。本PEP诞生的另一个原因是，PEP484中已经提到了在模块中\_\_getatter\_\_的相关用法。

此外，为了使dir() 可以显示已弃用和动态生成的属性，建议支持模块级别的\_\_dir\_\_函数。例如：

# lib.py
```python
deprecated_names = ["old_function", ...]
__all__ = ["new_function_one", "new_function_two", ...]

def new_function_one(arg, other):
   ...
def new_function_two(arg, other):
    ...

def __dir__():
    return sorted(__all__ + deprecated_names)
```
# main.py
```python
import lib

dir(lib)  # prints ["new_function_one", "new_function_two", "old_function", ...]
```
[详述](#详述)
=====================
module级别的\_\_getattr\_\_函数有一个入参，这个参数是被调用的属性的名称，返回相关值或者抛出异常AttributeError。
```python
def __getattr__(name: str) -> Any: ...
```
使用正常方式调用(object.\_\_getattribute\_\_)不到module中相关属性的时候，\_\_getattr\_\_将会在\_\dict\_\_中查找相关属性，如果也没有，则抛出异常AttributeError。如果找到，则赋予相关属性并返回结果。被查找的属性作为模块的全局变量会跳过\_\_getattr\_\_.这样做，是为了避免\_\_getattr\_\_作为内建函数浪费性能。

\_\_dir\_\_没有入参，返回值是一个字符串数组，该数组内容是该模块中可以访问的属性名:
```python
def __dir__() -> List[str]: ...
```

该函数会覆盖模块上的标准dir()方法。
范例可以在[[2]](#2)中找到。

[向下兼容性及性能相关](#向下兼容性及性能相关)
=====================
本PEP提到的做法，是会影响模块级别的属性管理(\_\_getattr\_\_,\_dir\_\_)。（但是语言上明确的将所有未登记的双下线名称进行了保留，并允许“无警告的破坏代码结构”，参看[[3]](#3)）。本PEP的影响程度其实很低，因为\_\_getattr\_\_方法只对查找不到的属性起作用。

一些模块和工具并不希望使用\_\_getattr\_\_，当然，这个问题已经不是第一次出现了。因为他们已经使用改写了\_\_getattr\_\_,\_dir\_\_的子模块替换模块。现在，因为本PEP，这个问题经更频繁的发生。


[注意事项](#注意事项)
=====================
模块的\_\_getattr\_\_需要确定自己访问的内容是存在并且有权限的。例如：最常用到的\_\_name\_\_属性，\_\_getattr\_\_是需要能访问到的。
```python
def keep_pickleable(func):
    func.__name__ = func.__name__.replace('_deprecated_', '')
    func.__qualname__ = func.__qualname__.replace('_deprecated_', '')
    return func

@keep_pickleable
def _deprecated_old_function(arg, other):
    ...
```
还要注意对类级别的\_\_getattr\_\_处理。避免类与模块之间的\_\_getattr\_\_相互调用。要使\_\_getattr\_\_对全局模块起作用（例如：需要懒加载子模块），可以参照以下的范例：
```python
sys.modules[__name__].some_global
```
或者
```python
from . import some_global
```

注意，第二种方法已经设置了模块属性，所以\_\_getattr\_\_只会被调用一次

[参考文献](#参考文献)
=====================
[1](#1)	PEP 484 section about \_\_getattr\_\_ in stub files (https://www.python.org/dev/peps/pep-0484/#stub-files)
[2](#2)	The reference implementation (https://github.com/ilevkivskyi/cpython/pull/3/files)
[3](#3)	Reserved classes of identifiers (https://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers)


[版权](#版权)
=====================
本文档已公开。
来源: https://github.com/python/peps/blob/master/pep-0562.rst




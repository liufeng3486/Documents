# PEP 553 -- Python新增内置函数breakpoint()

|PEP编号:|553|
|:----|:----|
|标题:|Python新增内置函数breakpoint()|
|作者:|Barry Warsaw <barry at python.org>|
|状态:|Final|
|类型:|Standards Track|
|创建时间:|2017-09-05|
|Python版本:|3.7|
|上传历史:|2017-09-05, 2017-09-07, 2017-09-13|
|决议:|https://mail.python.org/pipermail/python-dev/2017-October/149705.html|
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
本PEP建议增加一个新的内置函数breakpoint()，该函数被调用时，会进入Python debugger（译者：即我们常说的pdb）。此外，在sys中增加了两个新的方法，用来配置breakpoint的钩子(译者:\_\_breakpointhook\_\_和breakpointhook)

[理论基础](#理论基础)
=====================

一直以来，Python的标准库pdb中，都是有个很棒的调试器。通常是这么设置断点的：
```python
foo()
import pdb; pdb.set_trace()
bar()
```
这样，在执行foo()之后，执行bar()之前，Python会进入调试器。但是，这种方式存在几个缺点。

*  要打很多字（例子里打一个断点需要打27个字符）。
*  打字很容易出错。本PEP的作者，打这句话，时候会有问题，比如忘了打分号，或者将下划线达成了点号。
*  它不可配置，会直接使用pdb的调试器，不能使用其他调试器的选项。比如你使用的IDE或者其他开发环境。
*  Python的代码格式校验器（例如 flake8）会提示这句话有瑕疵，因为它包含两条语句。但是把它们单独写成两行，会有更多问题，因为在清楚断点的时候会更容易产生错误。简单来说，就是你需要删除断点的时候，可能只删除了其中的一行。

Python的开发人员还是有一些其他的调试程序可以选择的，但是记住如何调用他们是比较麻烦的。例如：即使是自带断点设置的IDE，如果只是编辑代码还是很方便的。这些不同的调试器从程序的角度而言，它们的调用方式（APIS）都不太一样，所以用户很难准确的记得，该怎么调用它们。

我们可以通过设置一个通用的调试程序API入口，来解决这个问题，这也是本PEP的目的。

[建议](#建议)
=====================
JavaScript语言中提供了调试语句[js-debugger]，当语句被调用时，会进入调试器。

本PEP提出新增一个内置函数breakpoint(),它被调用时，进入Python的调试器。所以，上面的例子就变成了这样：

```python
foo()
breakpoint()
bar()
```

此外，该PEP还为sys模块增加了两个新的内容，名为sys.breakpointhook()和sys.\_\_breakpointhook\_\_.在默认情况下，sys.breakpointhook()实现的是加载pdb和调用pdb.set_trace(),也可以设置成让breakpoint()调用其他的调试器。

sys.\_\_breakpointhook\_\_是用来初始化sys.breakpointhook()的设置的，这样，就可以很轻松的将sys.breakpointhook()恢复为初始化设置。（就像这样：sys.breakpointhook() = sys.\_\_breakpointhook\_\_）。这与已有的``sys.displayhook和sys.\_\_displayhook\_\_``还有 ``sys.excepthook()和sys.\_\_excepthook\_\_()``的工作方式完全相同[钩子]

内置函数breakpoint()的参数设置是这样的：breakpoint(*args, **kws)。位置参数与关键字参数是传给sys.breakpointhook()的，参数内容必须符合要求，不然会报错的。从sys.breakpointhook()获得的返回值，将传递给breakpoint()。

这是根据底层的调试器本身是接收一些可选参数的，比如：IPython允许用户在进入断点的时候，打印字符串[IPython embed]。从Python3.7开始，pdb模块还支持可选参数header[pdb header]。


[环境变量](#环境变量)
=====================
sys.breakpointhook()的默认设置，其实是依赖于一个名为PYTHONBREAKPOINT的环境变量，该环境变量可能是以下的各种值：
*  PYTHONBREAKPOINT=0  禁用调试器，具体来说，就是sys.breakpointhook()会返回None.
*  PYTHONBREAKPOINT= (空字符串)  这种情况与不设置该环境变量一样，此时，pdb.set_trace()照常运行。
*  PYTHONBREAKPOINT= 某个模块中的对象，比如some.importable.callable  在这个例子中， sys.breakpointhook（）首先import了some.importable。然后从中获取对象callable，调用它。也可以是一个不带点的字符串，在这种情况，比如PYTHONBREAKPOINT=int.(Guido偏好于Python的点式路径，而不是setuptools-style中entry_points的路径样式)
*  
当每次调用sys.breakpointhook()的时候，都会重读PYTHONBREAKPOINT。这样就允许了程序在运行期间变更调试器，breakpoint()有可能会去调用不同的调试器。这其实并不会对性能造成很大的影响，因为按照规则，进入调试器的时候，程序会暂停执行。所以，程序可以做如下的操作：

```python
os.environ['PYTHONBREAKPOINT'] = 'foo.bar.baz'
breakpoint()    # Imports foo.bar and calls foo.bar.baz()
```
重写sys.breakpointhook会破坏PYTHONBREAKPOINT的相关使用。如何重写取决于需要什么样的PYTHONBREAKPOINT。

对PYTHONBREAKPOINT的调用，不论是任何形式的失败（例如：导入失败，生成的模块包含不可用文件等），都抛出警告RuntimeWarning，并不进入断点。

值得注意是，与所有其他Python的环境变量一样，在以-E 参数运行解释器的时候，是会忽略用户对PYTHONBREAKPOINT的设置的。这意味着，此时PYTHONBREAKPOINT是默认值(即使用pdb，会调用pdb.set_trace())。有些观点认为当-E运行解释器，是否可以把PYTHONBREAKPOINT设置为0，但这些意见并没有得到统一。所以决定对这一特殊情况不做特殊处理。

[实施细节](#实施细节)
=====================
在建议实施中有一个pull请求。 [impl](#impl)

虽然是由C代码实现的，但是我们用Python的伪代码将功能做了如下的示例：

```python
# 在builtins.py中
def breakpoint(*args, **kws):
    import sys
    missing = object()
    hook = getattr(sys, 'breakpointhook', missing)
    if hook is missing:
        raise RuntimeError('lost sys.breakpointhook')
    return hook(*args, **kws)
```

```python
# 在sys.py中
def breakpointhook(*args, **kws):
    import importlib, os, warnings
    hookname = os.getenv('PYTHONBREAKPOINT')
    if hookname is None or len(hookname) == 0:
        hookname = 'pdb.set_trace'
    elif hookname == '0':
        return None
    modname, dot, funcname = hookname.rpartition('.')
    if dot == '':
        modname = 'builtins'
    try:
        module = importlib.import_module(modname)
        hook = getattr(module, funcname)
    except:
        warnings.warn(
            'Ignoring unimportable $PYTHONBREAKPOINT: {}'.format(
                hookname),
            RuntimeWarning)
    return hook(*args, **kws)

__breakpointhook__ = breakpointhook
```
[被拒的方案](#被拒的方案)
=====================

[新关键字](#新关键字)
--------------------
最初，作者的考虑是使用一个新的关键字，或者对某个原有关键字做拓展，比如break。但是这个方案被拒了。

* 新的关键字需要使用\_\_future\_\_(译者：调用它可以在旧版本中使用新特性)使其奏效。因为几乎任何新的关键字都可能与现有的代码存在冲突。这将使你无法轻松的进入调试器。

* 如果是扩展一个原有的关键字的话，比如break，这样易于阅读而且不需要使用\_\_future\_\_来绑定新的特性，但是如果PEP548中的建议一样，避免更多的扩展。

* 新的关键字需要修改语法，可能还需要增加新的字节码。这都使得它的实现更加复杂。但是新的内置函数却不会破坏现有的代码（因为任何现有的模块都会引用built-in），而且实现复杂度更低。

[sys.breakpoint()](#sys.breakpoint())
--------------------
为什么不是sys.breakpoint()呢？因为不是每个模块都会导入sys模块的。这只会使代码变得更多，会变成这样：

```python
import sys; sys.breakpoint()
```

这样的做法仍然存在本PEP需要解决的问题。

[版本历史](#版本历史)
=====================

* 2017-09-13
    * PYTHONBREAKPOINT环境变量被作为第一类特性。
* 2017-09-07
    * debug()更名为breakpoint()
    * 说明更改为breakpoint(*args, **kws),该断点函数将直接传递给sys.breakpointhook()

[参考](#参考)
=====================
|||
|:----|:----|
|[ipython-embed]|	http://ipython.readthedocs.io/en/stable/api/generated/IPython.terminal.embed.html|
|[pdb-header]|	https://docs.python.org/3.7/library/pdb.html#pdb.set_trace|
|[linters]|	http://flake8.readthedocs.io/en/latest/|
|[js-debugger]|	https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger|
|[hooks]|	https://docs.python.org/3/library/sys.html#sys.displayhook|
|[syntax]|	http://setuptools.readthedocs.io/en/latest/setuptools.html?highlight=console#automatic-script-creation|
|[impl]|	https://github.com/python/cpython/pull/3355|
|[envar]|	https://mail.python.org/pipermail/python-dev/2017-September/149447.html|

[版权](#版权)
=====================
本文档已公开。

源文: https://github.com/python/peps/blob/master/pep-0553.rst




PEP 567 -- Context Variables


PEP: 567

Title:  Context Variables

Author:Yury Selivanov <yury at magic.io>

Status:Final

Type:Standards Track

Created:12-Dec-2017

Python-Version:3.7

Post-History:12-Dec-2017, 28-Dec-2017, 16-Jan-2018



    
该PEP提出了一个新的contextvars模块和一组新的CPython C api来支持变量。这个概念线程本地存储(TLS)相似。但与TLS不同的是，它还可以跟踪每个异步任务的值，例如asyncio.Task。

这个建议是PEP 550的简化版本。 不同的是，这个PEP只关心异步任务的结果，而不是过程。对于内置的type都没有修改。

这个建议与Python的变量管理器没有严格的关系。它只是提供了一种机制，变量管理器可以使用这种机制来存储它们的状态。


API设计与修订


在Python 3.7.1中，所有变量C api的签名都被更改为使用PyObject *指针，而不是PyContext *、PyContextVar *和PyContextToken *，例如
        //in 3.7.0:
        PyContext *PyContext_New(void);
        
        // in 3.7.1+:
        PyObject *PyContext_New(void);

细节见[6]。显示了此PEP的C API的更新部分。

基本原理

对于在同一个OS线程中并发执行的异步任务，线程本地变量是不够的。任何使用thread .local()保存和恢复变量值的变量管理器在async/await 中使用时，其变量值都可能会被其它代码使用。

有几个这样的例子需要为异步编程提供变量本地存储：

变量管理器喜欢十进制变量和number .errstate。
与request相关的数据，如web应用程序中的token和header、gettext的语言环境等。
在大型代码库中进行分析、跟踪和日志记录。

介绍

	该PEP提出了一种新的变量管理机制。该机制涉及的关键类是contextvars.Context 和contextvars.ContextVar。该PEP还为在异步任务中使用该机制提出了一些方案。

	议的访问的变量机制使用ContextVar类。希望使用新的机制模块(例如decimal)应做到以下几点:
		声明一个全局变量，其中包含一个ContextVar作为主键;
		通过主键变量上的get()方法访问当前值;
		通过主键变量上的set()方法修改当前值。
		“当前值”的概念值得特别考虑:对于同一个键，在同时执行不同的异步任务时可能具有不同的值。这种思想在线程本地存储中是众所周知的，但在本例中，值的位置不一定绑定到线程。相反，他是存在“当前上下文”的概念，它存储在线程本地存储中。操作当前上下文是任务框架的职责，例如asyncio。

Context是ContextVar对象与其值的映射。它本身公开abc。映射接口(不是abc.MutableMapping!)，因此不能直接修改它。要为context的变量设置一个新值，用户需要:
	使用Context.run()方法使context对象“current”;
	使用context .set()为context变量设置一个新值。
	get()方法使用self键在当前context对象中查找变量。

不能直接引用当前context对象，但是可以使用Context .copy_context()函数来复制它。这确保Context.run()的调用者是其对象的唯一所有者。

详述
	
新增标准库模块contextvars, api如下:

1.copy_context() ->context函数用于为当前OS线程获取当前对象的副本。
2.用于声明和访问context变量的ContextVar类。
3.Context类封装context状态。每个OS线程都存储对其当前context实例的引用。直接控制该引用是不可能的。相反，context. run(callable，*args， **kwargs)方法被用于在另一个context中运行Python代码。


contextvars.ContextVar

ContextVar类具有以下函数签名:ContextVar(name， *， default=_NO_DEFAULT)。name参数用于调试，并公开为只读context .name属性。默认参数是可选的。例子:
    # Declare a context variable 'var' with the default value 42.
    var = ContextVar('var', default=42)

(_NO_DEFAULT是一个内部标记对象，用于检测是否提供了默认值。)

get(default=_NO_DEFAULT)返回当前context的值:

    # Get the value of `var`.
    var.get()

如果当前context中没有值，那么context .get()将:

返回get()方法的默认值(如果提供);或
返回context变量的默认值(如果提供);或
返回LookupError。

set(value) ->token用于为当前context的变量设置一个新值:
    # Set the variable 'var' to 1 in the current context.
    var.set(1)

ContextVar.reset(token)  被用来撤销set()操作，如果没有设置变量，则删除

    # Assume: var.get(None) is None
    
    # Set 'var' to 1:
    token = var.set(1)
    try:
        # var.get() == 1
    finally:
        var.reset(token)
    
    # After reset: var.get(None) is None,
    # i.e. 'var' was removed from the current context.

ContextVar.reset()异常抛出

使用另一个变量创建的token调用 抛出ValueError
如果当前context与创建token的context对象不匹配，则抛出ValueError
如果token对象已被重置一次，则出现RuntimeError。


contextvars.Token

contextvars.Token是一个不透明的对象，被用来将ContextVar恢复到它以前的值，如果之前没有设置变量，则将其从上下文中删除。它只能通过调用context .set()来创建。

为了调试和自检，它有以下几个属性
1.只读属性，指向创建token的变量var
2.只读属性，将old_value设置为变量在set()调用之前的值，或设置为Token。如果之前没有设置变量，则会丢失。

contextvars.Context

Context对象是context变量到值的映射。

Context()创建一个空值。要为当前OS线程获取当前context的副本，请使用Context .copy_context()方法:


    ctx = contextvars.copy_context()


要在某些conetext中运行Python代码，请使用Context.run()方法:
    
    ctx.run(function)

Function函数引起的任何context变量的更改都将包含在ctx context中:

var = ContextVar('var')
var.set('spam')

    def main():
        # 'var' was set to 'spam' before
        # calling 'copy_context()' and 'ctx.run(main)', so:
        # var.get() == ctx[var] == 'spam'
    
        var.set('ham')
    
        # Now, after setting 'var' to 'ham':
        # var.get() == ctx[var] == 'ham'
    
    ctx = copy_context()
    
    # Any changes that the 'main' function makes to 'var'
    # will be contained in 'ctx'.
    ctx.run(main)
    
    # The 'main()' function was run in the 'ctx' context,
    # so changes to 'var' are contained in it:
    # ctx[var] == 'ham'
    
    # However, outside of 'ctx', 'var' is still set to 'spam':
    # var.get() == 'spam'

当使用Context.run()从多个OS线程或者递归调用同一个context时抛出 RuntimeError。

Context.copy() 返回context对象的副本
context对象实现collections.abc。映射ABC。这可以用来内省 contexts:

    ctx = contextvars.copy_context()
    
    # Print all context variables and their values in 'ctx':
    print(ctx.items())
    
    # Print the value of 'some_variable' in context 'ctx':
    print(ctx[some_variable])

注意映射方法，包括Context.__getitem__ and Context.get, 忽略 context的默认值，（例如 context.default） 这意味着是一个用默认值创建的变量var，而不是在context中设置的

context[var]引发一个KeyError，
var在context中将返回False，
该变量不包括在context.items()中，等等。


asyncio

asyncio使用Loop.call_soon(), Loop.call_later(), and Loop.call_at()来调用异步执行的函数。Task uses call_soon()来调用包装好的协程。

我们修改Loop.call_{at,later,soon} and Future.add_done_callback() 来接受context可选的唯一关键参数，该参数默认为当前的context

    def call_soon(self, callback, *args, context=None):
        if context is None:
            context = contextvars.copy_context()
    
        # ... some time later
        context.run(callback, *args)

asyncio重的tasks需要维护他们自己的context，这些context时从创建他们的位置继承的，tasyncio.Task修改如下
    class Task:
        def __init__(self, coro):
            ...
            # Get the current context snapshot.
            self._context = contextvars.copy_context()
            self._loop.call_soon(self._step, context=self._context)
    
        def _step(self, exc=None):
            ...
            # Every advance of the wrapped coroutine is done in
            # the task's context.
            self._loop.call_soon(self._step, context=self._context)
            ...


执行

本节解释代码中的高级实现细节。为了使本节简短而清晰，省略了一些优化。

上下文映射是使用不可变字典实现的。这允许O(1)使用copy_context()函数。Hash Array Mapped Tries (HAMT)实现不可变字典的引用;HAMT性能[1]的分析见PEP 550。

在本节中，我们使用写时复制的方法和内置的dict类型实现了一个不可变的字典:

    class _ContextData:
    
        def __init__(self):
            self._mapping = dict()
    
        def __getitem__(self, key):
            return self._mapping[key]
    
        def __contains__(self, key):
            return key in self._mapping
    
        def __len__(self):
            return len(self._mapping)
    
        def __iter__(self):
            return iter(self._mapping)
    
        def set(self, key, value):
            copy = _ContextData()
            copy._mapping = self._mapping.copy()
            copy._mapping[key] = value
            return copy
    
        def delete(self, key):
            copy = _ContextData()
            copy._mapping = self._mapping.copy()
            del copy._mapping[key]
            return copy
	

每个OS线程都有一个对当前context对象的引用方法

    class PyThreadState:
        context: Context
    
contextvars.Context是 _ContextData的包装器

    class Context(collections.abc.Mapping):
    
        _data: _ContextData
        _prev_context: Optional[Context]
    
        def __init__(self):
            self._data = _ContextData()
            self._prev_context = None
    
        def run(self, callable, *args, **kwargs):
            if self._prev_context is not None:
                raise RuntimeError(
                    f'cannot enter context: {self} is already entered')
    
            ts: PyThreadState = PyThreadState_Get()
            self._prev_context = ts.context
            try:
                ts.context = self
                return callable(*args, **kwargs)
            finally:
                ts.context = self._prev_context
                self._prev_context = None
    
        def copy(self):
            new = Context()
            new._data = self._data
            return new
    
        # Implement abstract Mapping.__getitem__
        def __getitem__(self, var):
            return self._data[var]
    
        # Implement abstract Mapping.__contains__
        def __contains__(self, var):
            return var in self._data
    
        # Implement abstract Mapping.__len__
        def __len__(self):
            return len(self._data)
    
        # Implement abstract Mapping.__iter__
        def __iter__(self):
            return iter(self._data)
    
        # The rest of the Mapping methods are implemented
        # by collections.abc.Mapping.


contextvars.copy_context()实现如下


    def copy_context():
        ts: PyThreadState = PyThreadState_Get()
        return ts.context.copy()

   contextvars.ContextVar 与PyThreadState.context的交互

    class ContextVar:
    
        def __init__(self, name, *, default=_NO_DEFAULT):
            self._name = name
            self._default = default
    
        @property
        def name(self):
            return self._name
    
        def get(self, default=_NO_DEFAULT):
            ts: PyThreadState = PyThreadState_Get()
            try:
                return ts.context[self]
            except KeyError:
                pass
    
            if default is not _NO_DEFAULT:
                return default
    
            if self._default is not _NO_DEFAULT:
                return self._default
    
            raise LookupError
    
        def set(self, value):
            ts: PyThreadState = PyThreadState_Get()
    
            data: _ContextData = ts.context._data
            try:
                old_value = data[self]
            except KeyError:
                old_value = Token.MISSING
    
            updated_data = data.set(self, value)
            ts.context._data = updated_data
            return Token(ts.context, self, old_value)
    
        def reset(self, token):
            if token._used:
                raise RuntimeError("Token has already been used once")
    
            if token._var is not self:
                raise ValueError(
                    "Token was created by a different ContextVar")
    
            ts: PyThreadState = PyThreadState_Get()
            if token._context is not ts.context:
                raise ValueError(
                    "Token was created in a different Context")
    
            if token._old_value is Token.MISSING:
                ts.context._data = data.delete(token._var)
            else:
                ts.context._data = data.set(token._var,
                                            token._old_value)
    
            token._used = True


注意，在引用实现中，context .get()为最近的值提供了一个内部缓存，它允许绕过散列查找。这类似于decimal模块的从PyThreadState_GetDict()检索上下文的优化。在PEP 550，它详细解释了缓存的实现。

Token类实现如下

    class Token:
    
        MISSING = object()
    
        def __init__(self, context, var, old_value):
            self._context = context
            self._var = var
            self._old_value = old_value
            self._used = False
    
        @property
        def var(self):
            return self._var
    
        @property
        def old_value(self):
            return self._old_value


新api的摘要

Python API

1.一个新的contextvars模块，包含ContextVar、Context和token类，以及copy_context()函数。
2.xasyncio.Loop.call_at()、asyncio.Loop.call_later()、asyncio.Loop.call_soon()和asyncio.Future.add_done_callback()在它们被调用的上下文中运行回调函数。可以使用新的context关键字-only参数来指定自定义context。
3.asyncio.Task在内部修改，以维护自己的context

C API

1.PyObject * PyContextVar_New(char *name, PyObject *default):创建一个ContextVar对象。默认参数可以为NULL，这意味着该变量没有默认值。
2.int PyContextVar_Get(PyObject *， PyObject *default_value, PyObject **value):如果查找过程中出现错误，返回-1，否则返回0。如果找到context变量的值，它将被设为定义值。否则，将被设置为default_value，即便它不为NULL。如果default_value为NULL，那么value将被设置为变量的默认值，该变量也可以为NULL。value总是一个新的引用。
3.PyObject * PyContextVar_Set(PyObject *， PyObject *):设置当前context的变量值。
4.PyContextVar_Reset(PyObject *， PyObject *):重置context的变量值。
5.PyObject * PyContext_New():创建一个新的空context。
6.PyObject * PyContext_Copy(PyObject *):返回传递的context对象的副本。
7.PyObject * PyContext_CopyCurrent():获取当前context的副本。
8.int PyContext_Enter(PyObject *)和int PyContext_Exit(PyObject *)允许设置和恢复当前OS线程的上下文。需要始终还原以前的上下文:

    PyObject *old_ctx = PyContext_Copy();
    if (old_ctx == NULL) goto error;
    
    if (PyContext_Enter(new_ctx)) goto error;
    
    // run some code
    
    if (PyContext_Exit(old_ctx)) goto error;

被拒绝的想法

Replicating threading.local() interface

在PEP 550，其中详细讨论了这个主题:[2]。

Replacing Token with ContextVar.unset()

Token API允许使用context .unset()方法，这与PEP 550的链式context设计不兼容。如果需要在生成器和异步生成器中支持context变量，则需要与PEP 550的未来兼容性。

    token = cv.set(new_value)
    try:
        # cv.get() is new_value
    finally:
        cv.reset(token)

with:
    _deleted = object()
    old = cv.get(default=_deleted)
    try:
        cv.set(blah)
        # code
    finally:
        if old is _deleted:
            cv.unset()
        else:
            cv.set(old)

Having Token.reset() instead of ContextVar.reset()

Nathaniel Smith建议直接在Token类上实现context .reset()方法，因此:


    token = var.set(value)
    # ...
    var.reset(token)


我们将写成:
    token = var.set(value)
    # ...
    token.reset()

如果使用token .reset()，用户就不可能将另一个变量创建的token对象重置。

这个建议被拒绝的原因是使用context .reset()能够使读者更清楚地知道正在重置哪个变量。

使context对象可选

Antoine Pitrou提出，这可以支持透明的跨进程使用context对象，因此将执行任务转移到其他线程也可以使用ProcessPoolExecutor。


启用这个功能是有问题的，原因如下

1.	ContextVar对象没有_module__和_qualname__属性，因此不可能直接pickle context对象。这可以通过修改API来自动检测定义context变量的模块，或者向ContextVar构造函数添加一个只包含关键字的“module”参数来解决。

2.	并非所有context变量都引用picklable对象。将ContextVar设置为picklable必须是一个opt-in选项。
考虑到Python 3.7的发布时间，决定将这个建议推迟到Python 3.8。

使context具有MutableMapping

使context类实现abc。MutableMapping接口意味着可以使用Context[var] = value和del Context[var]操作设置和取消变量设置。

这个建议被推迟到Python 3.8+，原因如下:

1.如果在Python 3.8中决定生成器应该支持上下文变量(请参阅PEP 550和PEP 568)，那么上下文将被转换为上下文变量映射的链映射(因为每个生成器都有自己的映射)。这将使Context.__delitem__ 变得难以理解，因为它们只对链的最上面映射起作用。

2.只有一种方法可以修改context (context .set()和context .reset()方法)，这使得API更加直观。

例如，下面的代码片段与预期不一致的原因就不明显:

    var = ContextVar('var')
    
    ctx = copy_context()
    ctx[var] = 'value'
    print(ctx[var])  # Prints 'value'
    
    print(var.get())  # Raises a LookupError

而以下代码就正常

    ctx = copy_context()
    
    def func():
        ctx[var] = 'value'
    
        # Contrary to the previous example, this would work
        # because 'func()' is running within 'ctx'.
        print(ctx[var])
        print(var.get())
    
    ctx.run(func)


3.如果context是可变的，这意味着context变量可以与context中运行的代码单独(或同时)进行更改。这类似于从另一个正在运行的OS线程引用Python frame对象并修改它的f_local。只有一种方法可以为上下文变量赋值，这使得上下文在概念上更简单、更可预测，同时也为将来的性能优化打开了大门。

ContextVars具有初始值

Nathaniel Smith建议为ContextVar构造函数提供一个必需的initial_value关键字作为唯一参数。

反对该提议的主要理由是，对于某些类型，除了没有“初始值”之外，根本没有合理的“初始值”。例如，考虑一个将当前HTTP请求对象存储在上下文变量中的web框架。使用当前的语义，可以创建一个没有默认值的上下文变量:例如，考虑将当前HTTP请求存储在context变量中的web框架。使用当前的语义，可以创建一个没有默认值的上下文变量:
	
    
    # Framework:
    current_request: ContextVar[Request] = \
        ContextVar('current_request')
    
    
    # Later, while handling an HTTP request:
    request: Request = current_request.get()
    
    # Work with the 'request' object:
    return request.method


注意，在上面的示例中，不需要检查请求是否为None。只是希望框架总是设置current_request变量，或者它是一个bug(在这种情况下current_request.get()会引发LookupError)。

但是，如果我们有一个必需的初始值，我们就必须显式地防止没有值:

    # Framework:
    current_request: ContextVar[Optional[Request]] = \
        ContextVar('current_request', initial_value=None)
    
    
    # Later, while handling an HTTP request:
    request: Optional[Request] = current_request.get()
    
    # Check if the current request object was set:
    if request is None:
        raise RuntimeError
    
    # Work with the 'request' object:
    return request.method

此外，我们可以将context 变量与常规Python变量和thread .local()对象进行比较。它们都在查找失败时引发错误(分别是NameError和AttributeError)。

向后兼容性

这个建议保持了100%的向后兼容性

使用thread .local()存储context相关值的库，目前只能用于同步代码。将它们切换到使用的API上将保持它们对同步代码的行为不被修改，但将自动启用对异步代码的支持。

例子

Converting code that uses threading.local()

使用thread .local()的代码片段通常如下:

    class PrecisionStorage(threading.local):
        # Subclass threading.local to specify a default value.
        value = 0.0
    
    precision = PrecisionStorage()
    
    # To set a new precision:
    precision.value = 0.5
    
    # To read the current precision:
    print(precision.value)
    
这些代码可以转换为使用contextvars模块:
    
    precision = contextvars.ContextVar('precision', default=0.0)
    
    # To set a new precision:
    precision.set(0.5)
    
    # To read the current precision:
    print(precision.get())

将任务推给其他线程
可以使用当前线程的context副本在单独的OS线程中运行:

    executor = ThreadPoolExecutor()
    current_context = contextvars.copy_context()
    
    executor.submit(current_context.run, some_function)

参考实现

参考实现可以在这里找到:[3]。参见第32436期[4]。

验收
PEP 567于2018年1月22日星期一被Guido接受。参考实现在同一天合并。


参考
[1]  
https://www.python.org/dev/peps/pep-0550/#appendix-hamt-performance-analysis

[2]
https://www.python.org/dev/peps/pep-0550/#replication-of-threading-local-interface

[3]
https://github.com/python/cpython/pull/5027

[4]
https://bugs.python.org/issue32436

[5]
https://mail.python.org/pipermail/python-dev/2018-January/151878.html

[6]
https://bugs.python.org/issue34762
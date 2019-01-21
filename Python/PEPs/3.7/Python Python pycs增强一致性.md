# PEP 552 -- Python pycs增强一致性

|PEP编号:|552|
|:----|:----|
|标题:|pycs增强一致性|
|作者:|	Benjamin Peterson <benjamin at python.org>|
|状态:|Final|
|类型:|Standards Track|
|创建时间:|2017-09-04|
|Python版本:|3.7|
|上传历史:|2017-09-07|
|决议:|https://mail.python.org/pipermail/python-dev/2017-September/149649.html|
---
内容

*   [摘要](#摘要)
*   [理论基础](理论基础)
*   [详述](#详述)
*   [发布时间表](#发布时间表)
*   [3.8的新特性](#3.8的新特性)
*   [版权](#版权)

[摘要](#摘要)
=====================
本PEP建议对Pyc格式进行拓展，增加其确定性。

[理论基础](#理论基础)
=====================
构建的一致性[3](#3)是指相同的代码在不同的机器上运行会生成相同的字节文件。（当然，这些机器的环境设置一致或相似。）一致性对安全性而言很重要构建时，当输出内容是输入内容经过一系列可确定的变化之后得到的。保证其一致性是最有效的方案。它也是基于内容的构建系统中的关键概念之一，比如Bazel[4](#4)(译者：google的自动化构建工具)。

现在pyc格式封送处理的时候，会在数据的前缀增加magic number[7](#7)(译者:可以在importlib.util中找到MAGIC_NUMBER)、源时间戳和源文件大小。时间戳的存在意味着输入文件的内容是不确定的。输入内容是变化的，变化的地方是源时间戳。因此，生成的pyc是不一样的。

进行Python代码分发的时候一般只有一下几个选项：
* 1.不分发pycs，会失去缓存的优势
* 2.分发pycs,会失去一致性
* 3.给所有Python源码文件一个确定的时间戳（例如：https://github.com/python/cpython/pull/296）
* 4.混合使用1和2.例如在安装时生成pycs

这些方案都不太具有吸引力。本PEP建议使用一个确定的哈希值代替时间戳。当然，默认方式还是使用时间戳的方式。尽管使用时间戳保证pyc文件的有效性是存在不确定性的，但是在很多工作流以及案例中，这种方式很有效。基于哈希值的pyc格式，相对于基于时间戳的格式而言。对每个源文件进行哈希算法和读取文件的哈希值是会增加成本的。因此，目前，我们希望它主要用于分发工具和配置了相关选项的案例中。（注意：这里我们并没有完全解决pycs的一致性问题，因为还会有其他的问题[1](#1)[2](#2)）

[详述](#详述)
=====================
pyc的文件头是有3个32位的字符组成。我们把把它扩充为4个。第二个字段，从概念上将，应该是位字符。文件头的其他部分的解析和pyc文件是否失效，都取决于这个字符。

如果第二个字符是0，那么pyc是基于时间戳的，第三个字符和第四个字符分别是时间戳和文件大小。通过对源文件的数据和pyc文件头的内容对比，可以确定pyc是否有效。如果不是，那么pyc是基于源文件的hash值。我们将第二个字符设置为查看源文件的表示，第三和第四个字符组成一个64位的哈希值。会将源码文件经过SipHash[6](#6)生成一个哈希值。其他的快速哈希算法，比如MD5或者BLAKE2[5](#5)也是可以的，之所以选择SipHash是因为Python内置已经实现了它([详见PEP456](https://www.python.org/dev/peps/pep-0456/)),尽管SipHask的关键码值(key)是公开给Python的，但是这正方法的安全性是不存在问题的。尽管为了在一个受控的环境下用来校验,我们简化了部分内容。

当Python遇到基于哈希值的pyc时，文件头的第二个字符决定了Python的行为。Python会计算源文件的hash值与文件头的hash进行比较，来确定是否需要重新新生pyc文件。生成后，将重置文件头。

如果pyc不是基于哈希值的话，Python将不校验源文件的哈希值。这种情况下，一般是某个外部系统（例如：Linux的构建管理器）来校验pyc是否是最新的，所以Python本身不需要校验。就算不适用哈希值保持一致性，相关的文件头字段也需要正确设置，以便外部系统可以正确校验pyc。需要注意，即使是基于哈希值的pyc文件，仍然强制执行PEP3147的相关规定，及没有源文件的pyc文件将被强制执行。

py_compile 和 compileall 这两个API是用来生成基于哈希值的pyc文件。py_compile将新建一个枚举，这个枚举用来设置pyc的失效机制(代码如下)。
```python
class PycInvalidationMode(Enum):
    TIMESTAMP
    CHECKED_HASH
    UNCHECKED_HASH
```
py_compile.compile, compileall.compile_dir,和 compileall.compile_file 都会使用这个枚举的值。
编译工具将使用命令nenw进行扩展,--invalidation-mode 用来生成基于哈希值的pycs，无论是否设置校验的头文件的校验位。--invalidation-mode 一共有三个选项。分别是timestamp(默认值)，checked-hash，和unchecked-hash。这些内容都是对应PycInvalidationMode的枚举内容的。

importlib.util使用 source_hash(source)函数来计算源码的哈希值。

基于哈希值的pyc文件，失效配置使用check- hashbase -pycs。这是一个三态的选项。分别是：defualt,always和never。
* defualt 表示pyc中的哈希校验标识无效
* always 表示pyc文件总是无效，不校验相关值
* never 表示pyc文件一直有效

当check- hashbase -pycs = never 是，实际上，当机遇哈希值的pyc文件将重新生成，但是时间戳的pyc文件将不受影响。

Python3.8大约1-3个月进行一次BUG修复，持续18个月。在3.9.0 final版发布之后，将发布3.8的最后一版BUG修复版。之后，预计在之后的5年内只进行安全性更新。所以大概一直会持续到2024年10月。



[参考文献](#参考文献)
=====================
[1](#1)	http://benno.id.au/blog/2013/01/15/python-determinism
[2](#2)	http://bugzilla.opensuse.org/show_bug.cgi?id=1049186
[3](#3)	https://reproducible-builds.org/
[4](#4)	https://bazel.build/
[5](#5)	https://blake2.net/
[6](#6)	https://131002.net/siphash/
[7](#7)	https://docs.python.org/3/library/importlib.html#importlib.util.MAGIC_NUMBER



[致谢](#致谢)
=====================
感谢Gregory P. Smith、Christian Heimes和Steve Dower对本PEP做出的贡献

[版权](#版权)
=====================
本文档已公开。
来源: https://github.com/python/peps/blob/master/pep-0552.rst




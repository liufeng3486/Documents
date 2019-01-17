# PEP 221 -- Import As
# PEP 221 -- 导入为


|PEP编号:|221|
|:----|:----|
|标题:|Import As|
|作者:|thomas at python.org (Thomas Wouters)|
|状态:|Final|
|类型:|Standards Track|
|创建时间:|15-Aug-2000|
|Python版本:|2.0|
|上传历史|
---
内容

*   [介绍](#介绍)
*   [理论基础](#理论基础)
*   [实施细节](#实施细节)
*   [版权](#版权)
*   [参考](#参考)


[介绍](#介绍)
=====================
本篇PEP描述的Import as是针对Python2.0的建议。这个PEP用来追踪这个功能的状态和所有权，包含对这个功能的描述，并概括了支持这个功能需要进行的变更。这个文件的CSV版本修改记录包括所有历史记录。

[理论基础](#理论基础)
=====================
本篇PEP提出了关于Python中import，from \<module\> import  的扩展。

import将模块或者模块中的对象导入到本地。但是有时需要这些内容导入后的名称有所改变。比如存在名称冲突。这种需求可以通过使用下面的语句来实现。
```python
import os
real_os = os
del os
```
同样的，使用 from ... import 语句
```python
from os import fdopen, exit, stat
os_fdopen = fdopen
os_stat = stat
del fdopen, stat
```
建议的语法是，将as作为import的可选内容，如下：
```python
import os as real_os
from os import fdopen as os_fdopen, exit, stat as os_stat
```
as并不是一个预定的关键字，需要使用一些技巧来让cpython解析器使其奏效。对于很多高级的解析器而言，这应该不是问题。

导入子模块的时候情况比较特殊：
```python
import os.path
```
将os.path导入本地，而不是将os导入本地。
```python
import os.path as p
```
需要给别名的是os.path,而不是 os。上面的语句等价于:
```python
from os import path as p
```

[实施细节](#实施细节)
=====================
本篇PEP已经被接受，建议的代码已经被实现。补丁可以在SourceForge[1]_中找到。目前,语法中使用到的是一个NAME段，而不是单单一个字符串，是为了解决关键字的问题。引入了一个新的字节码IMPORT_STAR，用来执行 from module import *.更改了字节码IMPORT_FROM的行为，以便将请求的名称（始终是单个名称）加载到堆栈上，然后生成操作码STORE，由其进行存储。因此，现在所有显示导入都是与全局的。

from module import * 仍然是特殊的案例，因为它不兼容as语句，并不生成STORE操作码；导入的内容直接进入本地的命名空间，意味着这种导入方式始终是本地的，不是全局的。

也有人建议as之后，是一个表达式，而不是一个单独的名称。它可以使导入的内容变为需要的表达式。就像[2]_中所展示的一样，这样做的更改量是最低的，而且这样的结果是允许一些新的结构，就像一套新的Python赋值方式。然而，这个点子被guido拒绝，称其为“超泛化”。

[版权](#版权)
=====================
此文档已公开。

[参考](#参考)
=====================

.. [1] https://hg.python.org/cpython/rev/18385172fac0

.. [2] http://sourceforge.net/patch/?func=detailpatch&patch_id=101234&group_id=5470

源码: https://github.com/python/peps/blob/master/pep-0202.txt



## PEP 417 在标准库中包含mock

|PEP编号:|417|
|:----|:----|
| 标题：     | 在标准库中包含mock|
| 作者：      | Michael Foord <michael at python.org>   |
| 状态 :       |    Final   |
| 类型：        |    Standards Track   |
| 创建时间：        |    2012-03-12   |
| Python版本：        |    3.3   |
| 上传历史：        |  2012-03-12    |
| 决议：        | https://mail.python.org/pipermail/python-dev/2012-March/117507.html   |

内容
> * 介绍
> * 原理
> * 背景
> * 开放式问题
> * 参考
> * 版权

### 介绍
该PEP建议将mock [1]测试库作为unittest.mock添加到Python标准库中。

### 原理
创建用于测试的模拟对象是Python中常有的需求。许多开发人员根据需要在他们的测试套件中创建临时模拟。这是我们在Python测试套件中所做的，其中标准化的模拟对象库将更好的帮助我们。

目前有许多可用于Python的模拟对象库[2]，其中，mock是最流行的，PyPI上的下载数量与其他模拟库的总和相同。

mock的一个优点是它是一个模拟库而不是框架。它提供了一个可配置和灵活的模拟对象，而不需要考虑如何编写测试。mock api现在经过了良好的实战测试，并且很稳定。

mock还在测试范围内安全地处理monkeypatching和unkeypatching对象。这很难做到安全，许多开发人员/项目都在模仿这种功能(通常是不正确的)。执行此操作的标准化方法是，在描述符协议(etc)存在的情况下处理补丁的复杂性是有用的。人们要求一个“补丁”[3]功能进行单元测试。通过mock执行此操作。补丁比在unittest中重新实现此功能的一部分更可取。

### 背景
在2012年Python语言峰会上讨论并同意在Python标准库中添加mock。

### 开放式问题
从0.8版开始，这是写作时的当前版本，mock与Python 2.4-3.2兼容。Python标准库将允许删除一些特定于Python 2的“兼容性技巧”。

mock 0.8引入了一个新功能“auto-speccing”，废弃了一个名为“mocksignature”的旧模拟功能。在包含之前，可以完全从模拟中删除“mocksignature”功能。

### 参考
[1] [	mock library on PyPI](https://pypi.org/project/mock/ "With a Title")

[2] http://pypi.python.org/pypi?%3Aaction=search&term=mock&submit=search

[3] http://bugs.python.org/issue11664

### 版权
本文档已放在公共领域。

资料来源： https：//github.com/python/peps/blob/master/pep-0417.txt


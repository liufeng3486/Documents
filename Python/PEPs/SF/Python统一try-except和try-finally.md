## PEP 341 统一tyr-except and try-finally

|PEP编号:|341|
|:----|:----|
| 标题：     | 统一tyr-except and try-finally|
| 作者：      | Georg Brandl <georg at python.org>   |
| 状态 :       |    Final   |
| 类型：        |    Standards Track   |
| 创建时间：        |    2005-05-04   |
| 上传历史：        |       |

内容
> * 介绍
> * 原理/建议
> * 语法的变化
> * 实现
> * 参考
> * 版权

### 介绍
该PEP是建议修改try语句的语法和语义，以允许组合try- exception -finally模块。简而言之就是能够让以下写法有效:
```python
try:
    <do something>
except Exception:
    <handle the error>
finally:
    <cleanup>
```
### 原理建议
try-except语句和try-finally语句本身有很多使用场景，然而，使用时通常需要捕获异常并在事后执行一些清理代码。这有点麻烦，并且不是很容易理解，必须写成以下代码:
```python
f = None
try:
    try:
        f = open(filename)
        text = f.read()
    except IOError:
        print 'An error occurred'
finally:
    if f:
        f.close()
```
因此，有人提出这样一种结构，如下：
```python
try:
    <suite 1>
except Ex1:
    <suite 2>
<more except: clauses>
else:
    <suite 3>
finally:
    <suite 4>
```
于此种写法完全相同：
```python
try:
    try:
        <suite 1>
    except Ex1:
        <suite 2>
    <more except: clauses>
    else:
        <suite 3>
finally:
    <suite 4>
```
这是向后兼容的，并且合法的try语句今后将继续工作。

### 语法的变化
try语句的语法，目前为:
```python
try_stmt: ('try' ':' suite (except_clause ':' suite)+
        ['else' ':' suite] | 'try' ':' suite 'finally' ':' suite)
```
必须变成：
```python
try_stmt: 'try' ':' suite
        (
            (except_clause ':' suite)+
            ['else' ':' suite]
            ['finally' ':' suite]
        |
            'finally' ':' suite
        )
```
### 实现
由于PEP作者目前对CPython实现没有足够的知识，因此很遗憾，他无法交付一个CPython实现。Thomas Lee提交了一个补丁 [2].

然而，根据Guido的说法，实现[1]应该是小菜一碟--至少对于一个核心黑客来说是这样。

这个补丁是在2005年12月17日提交的，SVN修订版为41740[3]。

### 参考
[1] https://mail.python.org/pipermail/python-dev/2005-May/053319.html

[2] https://bugs.python.org/issue1355913

[3] https://mail.python.org/pipermail/python-checkins/2005-December/048457.html

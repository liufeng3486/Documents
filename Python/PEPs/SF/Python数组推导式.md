# PEP 202 -- Python数组推导式
PEP 202 -- List Comprehensions
===

|PEP编号:|202|
|:----|:----|
|标题:|数组推导式|
|作者:|barry at python.org (Barry Warsaw)|
|状态:|Final|
|类型:|Standards Track|
|创建时间:|13-Jul-2000|
|Python版本:|2.0|
|上传历史|
---
内容

*   [介绍](#介绍)
*   [解决方案](#解决方案)
*   [理论基础](#理论基础)
*   [例子](#例子)
*   [参考文献](#参考文献)
*   [Guido的声明](#Guido的声明)
*   [参考](#参考)


[介绍](#介绍)
=====================
本篇PEP描述了Python提供的一种拓展语法，字数组推导式。

[解决方案](#解决方案)
=====================
使用for和if通过一定条件构造数组，新数组的结构，将于for和if表现的结构一致。

[理论基础](#理论基础)
=====================
数组提供了一种简洁的新建方式，可以使用map(),filter() 以及相关嵌套循环来新建数组。

[例子](#例子)
=====================
```python
>>> print [i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```python
>>> print [i for i in range(20) if i%2 == 0]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```
```python
>>> nums = [1, 2, 3, 4]
>>> fruit = ["Apples", "Peaches", "Pears", "Bananas"]
>>> print [(i, f) for i in nums for f in fruit]
[(1, 'Apples'), (1, 'Peaches'), (1, 'Pears'), (1, 'Bananas'),
 (2, 'Apples'), (2, 'Peaches'), (2, 'Pears'), (2, 'Bananas'),
 (3, 'Apples'), (3, 'Peaches'), (3, 'Pears'), (3, 'Bananas'),
 (4, 'Apples'), (4, 'Peaches'), (4, 'Pears'), (4, 'Bananas')]
>>> print [(i, f) for i in nums for f in fruit if f[0] == "P"]
[(1, 'Peaches'), (1, 'Pears'),
 (2, 'Peaches'), (2, 'Pears'),
 (3, 'Peaches'), (3, 'Pears'),
 (4, 'Peaches'), (4, 'Pears')]
>>> print [(i, f) for i in nums for f in fruit if f[0] == "P" if i%2 == 1]
[(1, 'Peaches'), (1, 'Pears'), (3, 'Peaches'), (3, 'Pears')]
>>> print [i for i in zip(nums, fruit) if i[0]%2==0]
[(2, 'Peaches'), (4, 'Bananas')]
```
[参考文献](#参考文献)
=====================
List comprehensions become part of the Python language with release 2.0, documented in [1].

[Guido的声明](#Guido的声明)
=====================
上面的代码都是正确的。
错误的: [x, y for ...] ; 正确的 [(x, y) for ...].
这样的结构 [... for x... for y...] , 相当于两层for循环的嵌套。


[参考](#参考)
=====================
[1] http://docs.python.org/reference/expressions.html#list-displays
源码: https://github.com/python/peps/blob/master/pep-0202.txt



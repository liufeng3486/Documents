If
===
作为最基础的逻辑判断语句之一，If的基本逻辑和其它语言并没有什么本质的不同。但是有一些Python中比较有特色的用法。

### 基本用法
```python
if 条件一:
    # 满足条件一，dothing
elif 条件二 or 条件三：
    # 满足条件二或者满足条件三，dothing
elif 条件四 and 条件五:
    # 满足条件四并且满足条件五，dothing
else:
    #其他情况 dothing
```


### 嵌套
由于Python是使用换行及缩进来进行代码块区分的，所以，嵌套使用的时候，特别需要注意这一点。而且从Python对代码长度的规定来看，也是反对编写层级过多的代码。
```python
if 条件一:
    # 满足条件一，dothing
    if 条件二:
    # 满足条件一和条件二，dothing
    else :
    # 满足条件一旦不满足条件二，dothing
elif 条件三：
    # 不满足条件一 满足条件三，dothing
else:
    # 不满足条件一 也不满足条件三，dothing
```

当然在dothing的地方，再嵌套什么其他逻辑控制的语句都可以。

### 推导式中
[《PEP202数组推导式》](https://www.python.org/dev/peps/pep-0202/)，[《PEP274字典推导式》](https://www.python.org/dev/peps/pep-0274/)中介绍到，可以使用for和if进行一系列的数组，字典（PEP274虽然没有if的例子，但是却适用）的操作。

* 数组:
    ```python
    >>> print [i for i in range(20) if i%2 == 0]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    ```
* 字典
    ```python
    >>> someDict={1:2,3:4}
    >>> print {k : v for k, v in someDict.iteritems() if k==1}
    {1: 2}
    ```
    
### 注意事项
* if语句可以不包含elif和else。但是如果if语句里没有，有可能会造成逻辑漏洞,需要谨慎。
* 多次嵌套会增加代码的阅读难度。如果可以，尽量降低嵌套的层数。若，必须如此，尽量完善注释及变量名。
* if中的条件语句段，不要过于复杂。如果过长，可以将其单独作为一个变量，再判断变量的布尔值。

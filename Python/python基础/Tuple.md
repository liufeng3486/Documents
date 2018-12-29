Tuple
===
```python
class tuple(object):
```
从内建模块``builtins.py``的源码中可以看出，``tuple``的父类是``object``（python中的万年老父亲）。

**tuple 元组**
简单来说就是一个不能变更指向地址的数组,也不能添加，删除其中的元素

听上去有些拗口。因为以下的情况是可以变相改变元组的内容。
```python
list_temp = [2,3]
a =tuple([1,list_temp]) 
print (id(a[1]),a)  #2687647900232 (1, [2, 3])
list_temp.append(4)
print (id(a[1]),a)  #2687647900232 (1, [2, 3, 4])
```
从代码可以看出a[1]的地址没有变更多，但是内容变更了。



## 新建元组
+ 方法1：
```python
null_tuple = tuple()
not_null_tuple = tuple([1,2,3]) 
```
+ 方法2：
```python
null_tuple = ()  #获得一个空元组 null_tuple == ()
not_null_tuple = (1,2,3) #获得一个非空元组 not_null_tuple =(1,2,3)
```
从代码中可以看出，使用最原始的方式来实例化``list``类的方式更加繁琐，而且不能取得更好的效果。所以一般都会采用`方法2`.

## 遍历 元组  
+ 方法 1 #只遍历 值 
```python
tuple_1 = ("A","B","C")
for value in tuple_1:
    print value # >>"A" "B" "C"
```
+ 方法 2 可读性最好，但是比较繁琐
```python
tuple_1 = ("A","B","C")
for index in range(len(tuple_1)):
    print index,tuple_1[index]    # >>1，"A"   2，"B"   3，"C"
```
+ 方法 3 最常用
```python
tuple_1 = ("A","B","C")
for index,value in enumerate(tuple_1):
    print index,value    # >>1，"A"   2，"B"   3，"C"
```
遍历的方式其实和``list``一模一样

## 增:，元组复制，元组拼接
首先 元组没有办法添加元素
>**copy (1,2,3)**
+ 方法 1
```python
tuple_1 = (1,2,3)
tuple_2 = tuple_1    # id(tuple_1) == id(tuple_2)
```
+ 方法 2
```python
import copy
tuple_1 = (1,2,3)
tuple_2 = copy.copy(tuple_1)   # id(tuple_1) == id(tuple_2)
tuple_3 = (1,2,3)   # id(tuple_1) == id(tuple_3)
```
>**copy (1,2,3,[1,2,3])**
+ 方法 1
```python
tuple_1 = (1,2,3,[1,2,3])
tuple_2 = tuple_1    # id(tuple_1) == id(tuple_2)
```
+ 方法 2
```python
import copy
tuple_1 =  (1,2,3,[1,2,3])
tuple_2 = copy.copy(tuple_1)   # id(tuple_1) == id(tuple_2)
tuple_3 =  (1,2,3,[1,2,3])   # id(tuple_1) != id(tuple_3)  #这里的地址不一样哦
```
>**拼接 new_tuple =(1,2,3)+(4,5,6)**
+ 方法 1
```python
tuple_1 =  (1,2,3)
tuple_2 =  (4,5,6)
new_tuple = tuple_1 + tuple_2 
```
## 删:删除特定元素或者清空元组
除了重新赋值，没有办法实现。

## 改：变更元组内容
>**(1,2,3)->(1,2,3,4)**

除了重新赋值，没有办法实现。

>**(1,2,3,[1,2,3])->(1,2,3,[1,2,3,4])**
```python
list_1 = [1,2,3]
tuple_1 = (1,2,3,list_1)
list_1.append(4)
print (tuple_1)   # (1, 2, 3, [1, 2, 3, 4])
```
## 查：获取元组中的元素的个数，或者元素的编号
**(1,2,3,4,1)-> 获取1的下标**
+ 方法 1 正常方法
```python
tuple_1 = (1,2,3,4,1)
print(tuple_1.index(1)) #使用index() 但是只能获取第一个被查找到的index
```
+ 方法 2
```python
tuple_1 = (1,2,3,4,1)
for index,value in enumerate(tuple_1):
    if value == 1 :
        print (index)          #通过遍历的方式获取相应值的下标
```
**(1,2,3,4,1)-> 获取1的个数**
```python
tuple_1 = (1,2,3,4,1)
print(tuple_1.count(1)) #使用count()
```

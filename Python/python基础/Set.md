Set 集合 
===
```python
class Set(object)：
```
从内建模块``builtins.py``的源码中可以看出，``set``的父类是``object``（python中的万年老父亲）。

集合可以理解为一个没有重复元素的数组,而且``不支持切片和排序``。但是可以很方便的进行``集合运算``

**'set' object does not support indexing**
集合不支持index 比如没办法使用 set([1,2,3])[0]

**最常用的地方：数组去重**
```python
list_1 = [1,2,3,1,2,3]
list_1 = list(set(list_1)
print (list_1) #[1,2,3]
## 新建集合
```python
null_set = set()
not_null_set = set([1,2,3]) #获得一个非空集合 not_null_set = {1,2,3}
```
## 遍历 集合
```python
set_1 = set(["A" "B" "C"])
for value in set_1:
    print (value) # >>"A" "B" "C"
```
## 集合运算:集合类型的最方便的用处
**集合相减 A-A∩B**
a = {1,2,3,4,5}
b = {4,5,6,7,8} 
A-A∩B = {1,2,3}
+ 方法 1
```python
c = a - b
print(c) #{1,2,3}
```
+ 方法 2
```python
c = a.difference(b)
print(c) #{1,2,3}
```
+ 方法 3
```python
a.difference_update(b)
print(a) #{1,2,3}
```
**求并集 A∪B**
a = {1,2,3,4,5}
b = {4,5,6,7,8}
 A∪B={1, 2, 3, 4, 5, 6, 7, 8}
```python
c = a.union(b)
print(c) #{1, 2, 3, 4, 5, 6, 7, 8}
```
**求交集 A∩B**
a = {1,2,3,4,5}
b = {4,5,6,7,8}
A∩B={4, 5}
+ 方法 1
```python
c = a.intersection(b)
print(c) #{4, 5}
```
+ 方法 2
```python
a.intersection_update(b)
print(a) #{4, 5}
```
**判断交集是否为空**
+  A∩B!=None
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print (a.isdisjoint(b))   #False
```
+  A∩B==None
```python
a = {1, 2, 3}
b = {4, 5, 6}
print (a.isdisjoint(b))   #True
```
**子集判断 A⊆B**
a = {1,2}
b = {1,2,3}
A⊆B == True
```python
print (a.issubset(b))   #True
```
**A∪B-A∩B**
a = {1,2,3,4,5}
b = {4,5,6,7,8}
A∪B-A∩B={1, 2, 3, 6, 7, 8}
+ 方法 1
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = c.symmetric_difference(b)
print (c)   #{1, 2, 3, 6, 7, 8}
```
+ 方法 2
```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.symmetric_difference_update(b)
print (a)   #{1, 2, 3, 6, 7, 8}
```



## 增:集合增加元素，数组复制
>**{1,2,3}->{1,2,3,4}**
+ 方法 1
```python
set_1 = set([1,2,3])
set_1.add(4)
print(set_1)    # {1, 2, 3, 4} 
```
+ 方法 2 使用updata()
```python 
set_1 = set([1,2,3])
set_1.update({4})
print(set_1)     # {1, 2, 3, 4} 
```
>**copy {1,2,3}**
+ 方法 1
```python
set_1 = set([1,2,3])
set_2 = set_1   # set_1 与 set_2 地址一直相同，内容一直相同
set_1.add(4)  # set_1=={1,2,3,4} set_2=={1,2,3,4}
```
+ 方法 2
```python
set_1 = set([1,2,3])
set_2 = set_1.copy() # set_1 与 set_2 地址不相同，内容暂时相同
set_1.add(4)  # set_1=={1,2,3,4} set_2!={1,2,3,4}
```
+ 方法 3
```python
import copy
set_1 = {1,2,3}
set_2 = copy.copy(set_1)  #与 方法2 相同
set_2 = copy.deepcopy(set_1)  #与 方法2 相同
```
## 删:删除集合中特定元素或者清空集合
>**{1,2,3} -> {2,3}**
+ 方法 1
```python
set_1 = {1,2,3}
set_1.pop()   #出队，扔出第一个元素  
print(set_1) #{2,3}  这里pop出去的数据和数组表现形式不一样
```
+ 方法 2
```python
set_1 = {1,2,3}
set_1.remove(1) #因为集合本身就是去重的，所以remove虽然只能删除一个元素，不会发生有2个相同元素只删除1个的情况
print(set_1)   #{2,3} 如果删除一个不存在的元素会抛出异常 ``KeyError``
```
+ 方法 3
```python
set_1 = {1,2,3}
set_1.discard(1) # 和remove方法不同点，在于，可以尝试删除一个不存在的元素，而不会报错
set_1.discard(4) #不会报错
print(set_1)   #{2,3} 
```

>**清空集合 {1,2,3}->{}**
+ 方法 1
```python
set_1 = {1,2,3}
set_1.clear() #通过内建函数清空
```
+ 方法 2
```python
set_1 = {1,2,3}
set_1 = set() #直接重新赋值清空
```
## 改：变更元素内容
**{1,2,3}->{1,3,4} 只能删除后再添加**
```python
set_1 = {1,2,3}
set_1.remove(3)
set_1.add(4)
print(set_1) #{1,3,4}
```
**删除与其他集合重复的内容 A-A∩B**
{1,2,3} - {1,2,3}∩{2,3,4} = {1}
```python
set_1 = {1,2,3}
set_2 = {2,3,4}    #set_2 也可以是list,tuple
set_1.difference_update(set_2)
print(set_1)          #{1}
```



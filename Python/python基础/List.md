List
===
```python
class list(object)：
```
从内建模块``builtins.py``的源码中可以看出，``list``的父类是``object``（python中的万年老父亲）。

## 新建数组
+ 方法1：
```python
null_list = list()#获得一个空数组 null_list == []
not_null_list = list([1,2,3]) #获得一个非空数组 not_null_list = [1,2,3]
```
+ 方法2：
```python
null_list = []  #获得一个空数组 null_list == []
not_null_list = [1,2,3] #获得一个非空数组 not_null_list = [1,2,3]
```
从代码中可以看出，使用最原始的方式来实例化``list``类的方式更加繁琐，而且不能取得更好的效果。所以一般都会采用`方法2`.

## 遍历 数组
+ 方法 1 #只遍历 值 
```python
list_1 = ["A","B","C"]
for value in list_1:
    print value # >>"A" "B" "C"
```
+ 方法 2 可读性最好，但是比较繁琐
```python
list_1 = ["A","B","C"]
for index in range(len(list_1)):
    print index,list_1[index]    # >>1，"A"   2，"B"   3，"C"
```
+ 方法 3 最常用
```python
list_1 = ["A","B","C"]
for index,value in enumerate(list_1):
    print index,value    # >>1，"A"   2，"B"   3，"C"
```

## 增:数组增加元素，数组复制
>**[1,2,3] + [4] = [1,2,3,4]**
+ 方法 1
```python
new_list = [1,2,3] + [4]
```
+ 方法 2
```python
new_list = [1,2,3]
new_list.append(4)
```
+ 方法 3
```python
new_list = [1,2,3]
new_list.extend([4])
```
>**copy [1,2,3]**
+ 方法 1
```python
list_1 = [1,2,3]
list_2 = list_1   # list_1 与 list_2 地址一直相同，内容一直相同
list_1.append(4)  # list_1==[1,2,3,4] list_2==[1,2,3,4]
```
+ 方法 2
```python
list_1 = [1,2,3]
list_2 = list_1.copy() # list_1 与 list_2 地址不相同，内容暂时相同
list_1.append(4)  # list_1==[1,2,3,4] list_2!=[1,2,3,4]
```
+ 方法 3
```python
import copy
list_1 = [1,2,3]
list_2 = copy.copy(list_1)  #与 方法2 相同
list_2 = copy.deepcopy(list_1)  #与 方法2 相同
```
## 删:删除特定元素或者清空数组
>**[1,2,3] -> [1,2]**
+ 方法 1
```python
list_1 = [1,2,3]
list_1.pop()   #出栈，扔出最后一个元素
```
+ 方法 2
```python
list_1 = [1,2,3]
list_1.remove(3) #如果有多个3的话，只会删除第一个3
```
+ 方法 3
```python
list_1 = [1,2,3]
list_1 = list_1[:-1] #通过切片来删除最后一个元素
```
>**[1,2,3,3,3] -> [1,2]**
+ 方法 1
```python
list_1 = [1,2,3,3,3]
while 3 in list_1:
    list_1.remove(3)  #通过 value in list 来判断是否包含该元素
```
+ 方法 2
```python
list_1 = [1,2,3,3,3]
list_1 = list_1[:list_1.index(3)] #通过判断第一个3的下标来裁剪数组
```
>**清空数组 [1,2,3]->[]**
+ 方法 1
```python
list_1 = [1,2,3]
list_1.claer() #通过内建函数清空
```
+ 方法 2
```python
list_1 = [1,2,3]
list_1 = [] #直接重新赋值清空
```
## 改：变更元素内容
**[1,2,3]->[1,4,3]**
```python
list_1 = [1,2,3]
list_1[1] = 4
```
**数组排序 [4,8,0,2,1,7,6,5,3,9]->[0,1,2,3,4,5,6,7,8,9]**
```python
list_1 = [4,8,0,2,1,7,6,5,3,9]
list_1.sort()   #因为是通过ascii的大小，使用内建函数来排序
```
**['f','c','z','A','w','B']->['A', 'B', 'c', 'f', 'w', 'z']**
```python
list_1 = ['A', 'B', 'c', 'f', 'w', 'z']
list_1.sort()   #因为是通过ascii的大小，所以大写会在前面
```
**数组倒叙 [1,2,3,4,5]->[5,4,3,2,1]**
+ 方法 1
```python
list_1 = [1,2,3,4,5]
list_1 = list_1[::-1]   #通过切片，使用负的步长来完成翻转
```
+ 方法 2
```python
list_1 = [1,2,3,4,5]
list_1.reverse()   
```
## 查：获取数组中的元素，或者元素的编号
**['a','b','c']-> 获取`a`的下标**
+ 方法 1 正常方法
```python
list_1 = ['a','b','c']
print(list_1.index('a')) #使用index()
```
+ 方法 2
```python
list_1 = ['a','b','c']
for index,value in enumerate(list_1):
    if value == 'a' :
        print (index)          #通过遍历的方式获取相应值的下标
```
**['A','z', 'B', 'c', 'f', 'w', 'z']->获取'z'的下标** 
+ 方法 1 
```python
list_1 = ['a','b','c']
for index,value in enumerate:
    if value == 'a' :
        print (index)          #通过遍历的方式获取相应值的下标
```
+ 方法 2 
```python
a = ['A','z', 'B', 'c', 'f', 'w', 'z']
index = []
def getIndex(a,value,start=0):
    try:
        temp = a.index(value,start)
        index.append(temp)
        return getIndex(a,value,temp+1)  #使用递归+index来分段获取数据
    except:
        return index
print(getIndex(a,'z'))
```







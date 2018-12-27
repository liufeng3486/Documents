Dict Python 字典
===
```python
class dict(object)：
```
从内建模块``builtins.py``的源码中可以看出，``dict``的父类是``object``（python中的万年老父亲）。

和list不同的是，字典本身无序`python`，而且key唯一。
+ 无序：python3里的字典不像python2那样随性了，是根据赋值的顺序来决定输出的顺序的。
    + 但是任然没有很好的办法排序。
    + dict_1 = {"key1":"1","key3":3,"key2":2}  没有办法让dict_1变成  {"key1":"1","key2":2,"key3":3} 
+ key唯一:
```python
dict_1 = {"key1":1}
dict_1["key1"] = 11  #dict_1 != {"key1":11,"key1":1} 
print(dict_1)
```
与json之间的转换很方便``import json``
+ dict 转换为 json
```python
import json
dict_1 = {"key1":1,"key3":3,"key2":2,"dddkey3":3}
json_1 = json.dumps(dict_1)
print(type(json_1),json_1)
```
+ json 转换为 dict
```python
import json
json_1 = '{"key1": 1, "key3": 3, "key2": 2, "dddkey3": 3}'
dict_1 = json.loads(json_1)
print(dict_1,type(dict_1))
```
## 遍历 字典
+ 方法 1 只遍历key
```python
dict_1 = {"key1":1,"key2":2}
for key in dict_1:   #也可以用 for key in dict_1.keys():
    print (key)
```
+ 方法 2 只遍历value
```python
dict_1 = {"key1":1,"key2":2}
for value in dict_1.values():
    print (value)
```
+ 方法 3 遍历键值 使用key来获取value
```python
dict_1 = {"key1":1,"key2":2}
for key in dict_1:   #也可以用 for key in dict_1.keys():
    print (key，dict_1[key])
```
+ 方法 4 遍历键值 使用items获取 (key,value) 样式的元组
```python
dict_1 = {"key1":1,"key2":2}
for key,value in dict_1.items():   #也可以用 for key in dict_1.keys():
    print (key,value)
```

## 新建字典
+ 方法1：
```python
null_dict = dict() #获得一个空数组 null_dict == {}
not_null_dict = dict({"key":"value"}) #获得一个非空数组 not_null_dict = {"key":"value"}
```
+ 方法2：
```python
null_dict = {} #获得一个空数组 null_dict == {}
not_null_dict = {"key":"value"} #获得一个非空数组 not_null_dict = {"key":"value"}
```
+ 方法 3
```python
dict_1 = dict.fromkeys(("key1","key2","key3"),)
print (dict_1)   #{'key1': None, 'key2': None, 'key3': None}
dict_1 = dict.fromkeys(("key1","key2","key3"),[1,2])
print (dict_1) #{'key1': [1, 2], 'key2': [1, 2], 'key3': [1, 2]}
```
从代码中可以看出，使用最原始的方式来实例化``dict``类的方式更加繁琐，而且不能取得更好的效果。所以一般都会采用`方法2`.

方法3更多的使用在新建一个空字典，或者初始值一样的字典。这里存在一个小问题。就是
```python
dict_1 = dict.fromkeys(("key1","key2","key3"),[1,2])
print (id(dict_1["key1"]))
print (id(dict_1["key2"]))
```
这个问题主要涉及到，字典的值是某个数组的时候，指向的并不是值本身，而是地址。
## 增:字典增加元素，复制字典
>**{"key1":1,"key2":2} + {"key3":3} = {"key1":1,"key2":2,"key3":3}**
+ 方法 1  dict.update()
```python 
dict_1 = {"key1":1,"key2":2}
dict_2 = {"key3":3}
dict_1.updata(dict_2)
print(dict_1)
```
+ 方法 2 **kwargs 将字典转为关键字参数来重新实例化新的dict
```python
dict_1 = {"key1":1,"key2":2}
dict_2 = {"key3":3}
dict_new = dict(dict_1,**dict_2) # 等价于 dict(dict_1,key3=3)
print (dict_new)
```
+ 方法 3 for循环拼接
```python
dict_1 = {"key1":1,"key2":2}
dict_2 = {"key3":3}
for key,value in dict_2.items():
    dict_1[key]=value
print (dict_1)
```
>**copy {"key1":1,"key2":2}**
+ 方法 1
```python
dict_1 = {"key1":1,"key2":2}
dict_2 = dict_1   # list_1 与 list_2 地址一直相同，内容一直相同
dict_1["key1"]=3  # dict_1=={"key1":3,"key2":2} dict_2=={"key1":3,"key2":2}
```
+ 方法 2
```python
dict_1 = {"key1":1,"key2":2}
dict_2 = dict_1.copy() # list_1 与 list_2 地址不相同，内容暂时相同
dict_1["key1"]=3  # dict_1=={"key1":3,"key2":2} dict_2=={"key1":1,"key2":2}
```
+ 方法 3
```python
import copy
dict_1 = {"key1":1,"key2":2}
dict_2 = copy.copy(dict_1)  #与 方法2 相同
dict_2 = copy.deepcopy(dict_1)  #与 方法2 相同
```
## 删:删除特定元素或者清空字典
>**{"key1":1,"key2":2,"key3":3} -> {"key1":1,"key2":2}**
+ 方法 1
```python
dict_1 = {"key1":1,"key2":2,"key3":3}
dict_1.pop("key1")   #出栈，根据key扔出一对键值
print (dict_1)
```
+ 方法 2
```python
dict_1 = {"key1":1,"key2":2,"key3":3}
del dict_1["key1"] #使用del方法删除
print (dict_1)
```
+ 方法 3 不可取
```python
dict_1 = {"key1":1,"key2":2,"key3":3}
dict_1.popitem()    #和pop不同的是未指定key，由于字典本身是无序的，所以这种删除方式不可控
print (dict_1)
```
>**清空数组 {"key1":1,"key2":2,"key3":3}->{}**
+ 方法 1
```python
dict_1 = {"key1":1,"key2":2,"key3":3}
dict_1.clear() #通过内建函数清空
print (dict_1)
```
+ 方法 2
```python
dict_1 = {"key1":1,"key2":2,"key3":3}
dict_1 = {} #直接重新赋值清空
```
## 改：变更元素内容
**{"key1":1}->{"key1":10}**
+ 方法 1
```python
dict_1 = {"key1":1}
dict_1["key1"] = 10
```
+ 方法 2
```python
dict_1 = {"key1":1}
dict_1.updata(key1=10)
```
**{"key1":1,"key2":2,"key3":3}->{"key1":10,"key2":20,"key3":3}**
+ 方法 1
```python
dict_1 = {"key1":1,"key2":2,"key3":3}
dict_2 = {"key1":10,"key2":20}
dict_1.update(**dict_2)  #等价于  dict_1.update(key1=10,key2=20)
print (dict_1)
```
+ 方法 2
```python
dict_1 = {"key1":1,"key2":2,"key3":3}
dict_2 = {"key1":10,"key2":20}
for key,value in dict_2.items():
    if key in dict_1:
        dict_1[key] = value
print (dict_1)
```

**字典排序 {"key1":1,"key3":3,"key2":2}->{"key1":1,"key2":2,"key3":3}**
```python
没有很漂亮的方法 基本都是分割为keys(),values(),使用list.sort()来实现
```
## 查：获取数组中的元素，或者元素的编号
**{"key1":1,"key2":2}-> 获取`key1`的值**
+ 方法 1 
```python
dict_1 = {"key1":1,"key2":2}
print(dict_1.get("key1")) #的确有这么个方法，但是平时正常人类不用
```
+ 方法 2
```python
dict_1 = {"key1":1,"key2":2}
print(dict_1["key1"]) #这才是大家最熟悉的
```
**{"key1":2,"key3":3,"key2":2}->获取值为2的key** 
+ 方法 1  遍历获取key
```python
dict_1 = {"key1":2,"key3":3,"key2":2} 
print([key for key, value in dict_1.items() if value == 2])
----------------------
#为了便于大家理解
#以下等价于([key for key, value in dict_1.items() if value == 2]) 
key_list = []
for key ,value in dict_1.items():
    if value == 2:
        key_list.append(key)
print (key_list)
```
+ 方法 2 利用数组的index方法，我们这里复用了之前[Python基础/List](https://github.com/liufeng3486/Documents/blob/master/Python/python%E5%9F%BA%E7%A1%80/List.md) 中的一个函数 ``getIndex``
```python
dict_1 = {"key1":2,"key3":3,"key2":2} 
index_list = []
def getIndex(a,value,start=0):
    try:
        temp = a.index(value,start)
        index.append(temp)
        return getIndex(a,value,temp+1)  #使用递归+index来分段获取数据
    except:
        return index
index_list = getIndex(list(dict_1.values()),2)
for index in index_list :
    print(list(dict_1.keys())[index])
```

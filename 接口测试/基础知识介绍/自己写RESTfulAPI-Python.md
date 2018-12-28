自己写RESTfulAPI-Python
===
既然要自己写一个符合RESTful风格的WEB应用，那么就需要选择一门语言+一个WEB应用框架。

语言：由于这里更多的受众是测试这个群体，所以选用的是测试使用占比最高的语言``Python``。

WEB应用框架：Python的WEB应用框架也有很多，web2py,flask,django..... 虽然很喜欢用django，但是由于它的MVT结构，不便于方便用一个PY文件展示内容。所以在这里，我们选用了``flask``

## 准备
+ Python 安装
    + [Windows](http://Windows)
    + [Mac](http://Mac)
+ Flask 安装
    ```python
    pip install flask
    ```
## 新建一个WEB应用
我们先搭建一个本地WEB应用，让大家能通过浏览器访问到自己的制作的页面。
+ test_1.py
```python 
from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run()
```
执行test_1.py后，我们可以获得下面的输出
```
>>>* Serving Flask app "test_1" (lazy loading)
>>>* Environment: production
>>>   WARNING: Do not use the development server in a production environment.
>>>   Use a production WSGI server instead.
>>> * Debug mode: off
>>> * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
此时，我们根据输出的提示，再浏览器地址栏输入 http://127.0.0.1:5000/ 

![Image text](https://raw.githubusercontent.com/liufeng3486/Documents/master/%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E4%BB%8B%E7%BB%8D/_static/screenshot/RESTfulAPI-Python_Start.png)



可以看到，很简单的几行代码，我们就获得一个WEB应用，之后我们再这个基础上做一些丰富

## 编写接口

我们按照下面的接口列表来进行编写的工作

|Method|URL|行为|Function Name|
|:----:|:----|----:|----:|
|GET|http://127.0.0.1:5000/api/v1.0/tasks|查询列表|getTasks|
|GET|http://127.0.0.1:5000/api/v1.0/tasks/[task_id]|查询详单|getTaskById|
|POST|http://127.0.0.1:5000/api/v1.0/tasks|创建/更新|createTask|
|PUT|http://127.0.0.1:5000/api/v1.0/tasks/[task_id]|更新|updataTask|
|DELETE|http://127.0.0.1:5000/api/v1.0/tasks/[task_id]|删除|deleteTask|


为了便于理解和简化工作量，我们这里就不使用数据库了。我们使用一个字典来管理数据。

```python
from flask import Flask, jsonify,make_response,request
app = Flask(__name__)
path = '/api/v1.0'
tasks = [    #这是我们的数据
    {
        'id': 1,
        'data': 'data_1',
    },
    {
        'id': 2,
        'data': 'data_2',
    }
]

@app.route(path + '/tasks', methods=['GET'])  #获取全部列表
def getTasks():
    return jsonify({"tasks":tasks})

@app.route(path + '/tasks/<int:task_id>', methods=['GET']) #获取相应ID的列表
def getTaskById(task_id):
    for solo in tasks:
        if solo["id"] == task_id:
            return jsonify({"tasks":solo})
    return not_found({'error': 'Not found'})

@app.route(path + '/tasks', methods=['POST']) #创建新数据
def createTask():
    if not request.json or not 'data' in request.json: #入参判断
        return error_request("Resquest Data Error")
    task = {
        'id': tasks[-1]['id'] + 1,  #ID自增
        'data': request.json['data'],
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route(path + '/tasks/<int:task_id>', methods=['PUT'])  #更新数据
def updataTask(task_id):
    if not request.json or not 'data' in request.json : #入参判断
        return error_request("Resquest Data Error")
    for solo in tasks:  
        if solo["id"] == task_id:  #id遍历查询
            solo["data"] = request.json["data"] #更新数据 
            return jsonify({"tasks":tasks})     
    return not_found("id %s not found"%(str(task_id))) #未找到相关id 返回 404

@app.route(path + '/tasks/<int:task_id>', methods=['DELETE'])  #删除数据 
def deleteTask(task_id):
    for solo in tasks:
        if solo["id"] == task_id:
            tasks.remove(solo)
            return jsonify({"tasks":tasks})
    return not_found("id %s not found"%(str(task_id)))

@app.errorhandler(404)   #重写404
def not_found(error):
    return make_response(jsonify(error), 404)
@app.errorhandler(400)  #重写400
def error_request(error):
    return make_response(jsonify(error), 400)

if __name__ == '__main__':
    app.run()
```
以上是全部代码。运行后，就可以在通过相关地址来访问这些接口了。

## 测试一下
为了方便大家使用，已经制作好了相应POSTMAN数据，可以再运行以上代码启动WEB服务后，在POSTMAN里导入
[Test PostMan Data 右键另存为](https://raw.githubusercontent.com/liufeng3486/Documents/master/%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E4%BB%8B%E7%BB%8D/_static/files/RESTful_Flask_Demo.json.postman_collection)
就可以获得下图的内容,并直接进行测试
![Image text](https://raw.githubusercontent.com/liufeng3486/Documents/master/%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E4%BB%8B%E7%BB%8D/_static/screenshot/RESTfulAPI-Python_PostMan.png)

## 让其他人访问到
从接口地址可以看到，我们给出的地址都是127.0.0.1的形式，都是本地地址。这种地址局域网里的其他伙伴是没有办法访问到的，为了让我们的WEB服务别人也能访问到，我们需要在启动flask的地方做一些修改
还是用我们的第一个demo做范例来说明
+ test_1.py
```python 
from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
这样的话，别人就能通过 http://本机的IP地址:5000/api/v1.0/...  来访问你新搭建的WEB应用。
+ 本机的IP地址
    + Windows 通过cmd Ipconfig 来获取 
    + Mac 通过cmd ifconfig 来访问


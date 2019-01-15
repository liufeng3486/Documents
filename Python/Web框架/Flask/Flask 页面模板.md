
Flask 使用页面模板
===
# 介绍
在ide中新建flask项目的时候，一般除了.py文件外，还会新建两个空文件夹，其中一个名为``templates``
顾名思义，这个文件夹是用来放置html模板的。
很多情况下，web应用是需要使用到html模板的，例如列表展示，订单展示。。。以及非常多涉及到数据展示的页面。都需要使用到模板。
简单来说模板就如同货架一般，我们只要按照规定的格式往其中塞商品就可以了。

# 调用模板
秉承着一贯的原则，我们在这里给出使用模板的极简demo
这里需要注意的是，``static``,``templates``这两个文件夹内容的路由匹配是Flask自动处理的。不需要用户过多参与。
### Demo

```shell
/
├─static  #静态文件 (空文件夹，没有该文件夹也可以)
├─templates #y页面模板
│    └─ index.html
└─test.py  
```
### /templates/index.html  
```html  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    {{ name }}  
</body>
</html>
```
### /test.py
```python
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',
                            name = "testname"     #在这里传递数据至html模板
                           )


if __name__ == '__main__':
    app.run()

```
这个时候，访问 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)我们就可以看到testname显示到了页面上，这个例子看上去很画蛇添足。只是把一段字符串显示到页面上。我们绕了很多弯路。但是。换一个复杂点的例子，就可以看出这样做的好处了。

### Demo 2 
```shell
/
├─static  #静态文件 (空文件夹，没有该文件夹也可以)
├─templates #y页面模板
│    └─ index.html
└─test.py  
```
### /templates/index.html  
这是一个来自于[w3school](http://www.w3school.com.cn/tiy/t.asp?f=html_lists_nested)的教学案例，我们再这里做了一点点改动
```html
<html>
<body>

<h4>一个嵌套列表：</h4>
<ul>
  <li>人物
    <ul>
    <li>{{name}}</li>
    <li>{{age}}</li>
    </ul>
  </li>
</ul>

</body>
</html>
```
### /test.py
```python
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',
                            name = "testname",     #在这里传递数据至html模板
                            age = "22"
                           )


if __name__ == '__main__':
    app.run()

```
执行这个例子可以看到，页面不仅是展示了两个字符串，还附带着一定的格式。这在平时使用的时候是必然优于直接返回string，或者整个html的文本段方式。

# Flask 模板语法
模板中对于数据的显示，除了直接的字符串替换以外。有时候还需要进行一定的逻辑控制。相关内容，详见:[Flask 模板语法](https://github.com/liufeng3486/Documents/blob/master/Python/Web%E6%A1%86%E6%9E%B6/Flask/%E6%A8%A1%E6%9D%BF%E8%AF%AD%E6%B3%95.md)





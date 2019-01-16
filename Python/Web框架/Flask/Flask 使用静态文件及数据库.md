Flask 使用静态文件及数据库
===
# 介绍
作为网页的三大语言``html``,``css``,``js``。``html``[使用页面模板](https://github.com/liufeng3486/Documents/blob/master/Python/Web%E6%A1%86%E6%9E%B6/Flask/Flask%20%E9%A1%B5%E9%9D%A2%E6%A8%A1%E6%9D%BF.md)可以进行简化。简单的``css``和``js``也可以直接写在.html中。但是很多时候，项目中的``css``和``js``是很复杂，而且有些是其他人提供的，我们只要使用``script``和``link``标签，就可以很方便的加载.js和.css。当然，除了这些文件以外，还有各种静态文件，比如.icon,.png.....

作为正常的web应用，数据库的支持是必不可少的，在这里也做出简单的使用说明。

# 加载静态文件
我们假设需要加载的文件名为 test.css 内容
### Demo

```shell
/
├─static  #静态文件 (空文件夹，没有该文件夹也可以)
│    ├─ test1.css
│    └─ test2.css
├─templates #页面模板
│    └─ index.html
└─test.py  
```
### /static/test1.css  
这是一极其简单的css，效果是把body标签里的文字变成红色。
```css
body{color:red}
```
### /static/test2.css  
这是另一个css文件，效果是把body标签的背景色变成黑色。
```css
body{background-color:black}
```
### /templates/index.html  
以下的两种方式，都可以用来加载静态文件
```html  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="static/test1.css"><!--这是一种加载方式。-->
    <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='test2.css')}}"><!--这是另种加载方式。-->
    <title>Title</title>
</head>
<body>
    {{ name }}  
</body>
</html>
```
### /test.py
和之前的例子一样，这里完全没有改变
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
这个时候，访问 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)我们就可以看到testname显示到了页面上。而且背景和字体颜色都有所改变。如果显示有问题，可以先清理下浏览器缓存。

由上面的例子可以看出第一种方式进行静态文件加载其实更加简单，但是flask的官方文档似乎更推荐使用第二种方式。

# 连接数据库








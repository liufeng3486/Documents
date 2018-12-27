RESTful API介绍
===
相对于这个名字来说，大家更熟悉的是HTTP接口。比如，GET,POST,PUT....

这二者之间其实是存在紧密联系的。
但是！
>REST != HTTP
#### 与HTTP请求的关系
首先我们先看名字RESTfulAPI。意思是符合RESTful风格的接口。

所谓RESTful并不是一种协议或者一种硬性的要求。而是一种风格。

RESTfulAPI与之关联最大的就 [Ajax](http://)。在大部分的情况下，他们二者结合在一起。使服务端与客户端之间的数据传输更加简单、清晰。

废话那么多，用简单的话来说就是，这是对HTTP规范的一种应用方式，因为这不是一套标准，而是一套风格。所以我们经常能听到，别人说：“这是RESTful风格的。”

``method(GET,POST,PUT,DELETE..)代表动作``，``url地址代表一个资源``
  + ``method:``GET 表示获取资源，POST 表示新建/更新资源， PUT 表示更新资源， DELETE 表示删除资源
  + ``url:``一个地址，也是一个资源，所以在命名时，更多是使用名词来描述这个资源是什么。

#### 与代码之间的关系
其实与代码之间没什么关系，所以能写服务端的语言，都能写出RESTful风格的API。

包括但不限于``.net`` ``java`` ``python`` ``ruby`` ``php`` ``node.js`` ``....``

除了不限于代码以外，同样不限于各种 Web 应用框架，

包括但不限于``django`` ``flask`` ``zendframwork`` ``ThinkPHP`` ``spring MVC`` ``JSF ``

简单来说，用中文，英文，法语都能说土味情话。

### RESTfulAPI 长什么样子
传输的数据基本都是``json``,所以在请求的``headers``里，一般都是 ``"contentType": "application/json",``

这是`符合RESTful风格`的。是否有版本号并不一定，也有些情况是将版本号放在headers中。

|Method|URL|行为|
|:----:|:----|----:|
|GET|http://www.xxx.com/api/v1.0/tasks|查询列表|
|GET|http://www.xxx.com/api/v1.0/tasks/task_id|查询详单|
|POST|http://www.xxx.com/api/v1.0/tasks|创建/更新|
|PUT|http://www.xxx.com/api/v1.0/tasks/task_id|更新|
|DELETE|http://www.xxx.com/api/v1.0/tasks/task_id|删除|

这是`不符合RESTful风格`的，在日常工作中大家肯定经常看到这样的URL

|Method|URL|行为|
|:----:|:----|----:|
~~|GET|http://www.xxx.com/api/gettasks|查询列表|
|GET|http://www.xxx.com/api/getdetal_id|查询详单|
|POST|http://www.xxx.com/api/createtask|创建/更新|
|PUT|http://www.xxx.com/api/tasks/updatetask|更新|
|DELETE|http://www.xxx.com/api/tasks/deltask|删除|~~

除了URL的问题，在日常工作中，经常见到接口的名字叫``http://www.xx.com/getdetail``，然后使用的是``POST``方法。非常的.....这种情况，居然还号称自己是RESTful风格。

### 更多
更多的内容可以访问 [restfulapi官网](https://restfulapi.net/)

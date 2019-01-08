接口SOAP RESTFUL RPC说明
===
在这里，我们要说的不是GET,POST这些不同method的区别。而是关于soap,RESTful,rpc... 

当然，现在绝大部分需要测试关心，和测试过程中遇到的接口都是HTTP的接口，但是也有一些区分。由于国内互联网过于"敏捷"的特点。使开发人员并没有足够的时间，按照相关的规范及风格来设计自己的接口。造成，现在大家在测试过程中能看到的接口都有些四不像的味道,特别是RESful风格的接口。

作为测试人员，首先，我们应该知道每种风格、类型的接口应该长成什么样子。这样，我们才能更好的给开发人员定义BUG。

比如 一个是restful风格的服务，开发给出了一个名为 ../getData 的接口。这个时候，作为测试人员，是可以提出低级别的BUG给相关开发的。当然，如果公司使用BUG相关数据作为开发的绩效指标之一（这个行为的确不人道，但是确实存在。），这个时候测试人员应该更加人性化的，不是提BUG，而且一个 "优化建议" 。在其中，告诉开发，这样的命名和使用并不符合相关风格。

以上的例子，在短期内，对于项目的贡献度其实是极低的，但是对于测试人员自身的素质要求，确实高于平均值的。而且可以提高这个测试人员，在相关人员心中的技术地位。

想要提出这样的优化建议，是需要一定的知识和项目经验积累。

### SOAP
由于.net兴起而发展起来的一套标准。卖点主要是，可以兼容所有操作系统和技术栈。

关键词:``XML``

通俗点说SOAP就是通过HTTP来发送XML格式的内容。来进行信息的传递。

##### SOAP Demo
**请求：**
```shell
POST /SoapAPI HTTP/1.1
Host: www.example.org
Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

  <soap:Body xmlns:m="http://www.example.org/stock">
    <m:GetStockPrice>
      <m:StockName>IBM</m:StockName>
    </m:GetStockPrice>
  </soap:Body>
  
</soap:Envelope>
```
**响应**
```shell
HTTP/1.1 200 OK
Content-Type: application/soap+xml; charset=utf-8
Content-Length: nnn

<?xml version="1.0"?>
<soap:Envelope
xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">

  <soap:Body xmlns:m="http://www.example.org/stock">
    <m:GetStockPriceResponse>
      <m:Price>34.5</m:Price>
    </m:GetStockPriceResponse>
  </soap:Body>
  
</soap:Envelope>
```

### RPC
相对于SOAP而言，RPC更加简单，从相关的规范说明文档长度上就可以看出来。RPC相关文档的页数大概只有SOAP的1/7。

从传递的内容来看，更多的也是使用HTTP POST来传输xml。
**请求**
```shell
POST /RpcAPI HTTP/1.1
Host: www.example.org

<?xml version="1.0"?>
<methodCall>
   <methodName>GetSPrice</methodName>
   <params>
      <param>
         <value><string>Value</string></value>
      </param>
   </params>
</methodCall>
```
**响应**
```shell
HTTP/1.1 200 OK
<?xml version="1.0"?>
<methodCall>
   <methodName>GetPrice</methodName>
   <params>
      <param>
         <value><double>66.66</double></value>
      </param>
   </params>
</methodCall>
```

### RESTful 
相对于之前的二者而言，它更加依赖于http提供规范。

他的传输内容，更多的是``JSON``，而不是xml

而且一个url代表一个资源，请求的method则是对资源的操作行为。

简单来说就是：对``资源``(url)做``某个类型的操作``(method)的操作 

**请求**
```shell
GET /Price?Name=Value HTTP/1.1
Host: www.example.org
```
**响应**
```shell
HTTP/1.1 200 OK
<?xml version="1.0"?>
<m:Price xmlns:m="http://www.example.org/Price">66.66</m:Price>
```

具体的内容可以转到 
[RESTful API 介绍](https://github.com/liufeng3486/Documents/blob/master/%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95/%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86%E4%BB%8B%E7%BB%8D/RestfulAPI.md)


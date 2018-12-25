# PyPi 源更改

**国内源**

+ 豆瓣
    + ``地址`` https://pypi.douban.com/simple/ 
    + ``语句`` pip install -i  https://pypi.douban.com/simple/ PackageName
+ 阿里云 
    + ``地址`` http://mirrors.aliyun.com/pypi/simple/
    + ``语句`` pip install -i  https://pypi.douban.com/simple/ PackageName
+ 清华大学 
    + ``地址`` https://pypi.tuna.tsinghua.edu.cn/simple/
    + ``语句`` pip install -i  https://pypi.tuna.tsinghua.edu.cn/simple/ PackageName
+ 中国科学技术大学 
    + ``地址`` https://pypi.tuna.tsinghua.edu.cn/simple/
    + ``语句`` pip install -i  https://pypi.tuna.tsinghua.edu.cn/simple/ PackageName
 + ~~中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/~~

**临时**

    pip install -i 地址 包名
    
**永久**
+ Linux
    + 修改~/.pip/pip.conf(或者创建一个),将index-url变量修改为所要更换的源地址:



     [global]
      index-url = https://pypi.tuna.tsinghua.edu.cn/simple
　
+ windows
    + user目录中创建一个pip目录,如C:\Users\xx\pip，新建文件pip.ini,内容如下：
    

    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  


### 介绍
``PyPi`` == ``Python Package Index``
官网地址 == https://pypi.org/
这个站点是做什么的，网站首页的自述写的很明白：查找，安装以及开源python包。
所以平时说到的python有非常多的轮子，这些轮子就在这里。


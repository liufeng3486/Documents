# loguru日志模块一个完全可以取代buildin logging module的日志模块
## 简单实践
首先，你要安装
```
pip install loguru
```
loguru的主要概念只有一个日志记录器。
为了方便起见，它首先被预先配置并输出到stderr(但这是完全可配置的)。
从loguru导入日志记录器
最简单实践一下：
```python
from loguru import logger
logger.info("this is so easy!")
```
输出：
```
2019-01-04 14:15:26.936 | INFO     | __main__:<module>:20 - this is so easy
```
是不是比内建logging日志模块简单很多？
## 没有 Handler,  Formatter, Filter: 仅仅一个函数解决所有日志配置
如何添加处理程序？如何设置日志格式？如何过滤邮件？如何设定水平？
一个答案：add()功能。
```python
logger.add（sys.stderr，format = " {time}  {level}  {message} "，filter = " my_module "，level = " INFO "）
```
此函数应用于注册接收器，该接收器负责管理使用记录字典进行上下文化的日志消息。接收器可以采用多种形式：简单函数，字符串路径，类文件对象，内置处理程序或自定义类。
## 使用旋转/保留/压缩更轻松地进行文件记录
如果要将记录的消息发送到文件，则只需使用字符串路径作为接收器。为方便起见，它也可以自动定时：
```python
logger.add（“ file_ {time} .log ”）
```
如果您需要旋转记录器，如果要删除旧日志，或者希望在关闭时压缩文件，也可以轻松配置它。
```
logger.add（“ file_1.log ”，rotation = “ 500 MB ”）     ＃自动ratate太大的文件 
logger.add（“ file_2.log ”，rotation = “ 12:00 ”）      ＃每天中午创建新文件 
logger.add（“ file_3.log ”，rotation = “ 1周”）     ＃文件太旧后，它会被旋转
logger.add（“ file_X.log ”，retention = “ 10天”）   ＃一段时间后清理
logger.add（“ file_Y.log ”，compression = “ zip ”）     ＃保存一些喜爱的空间
```
## 使用大括号样式的现代字符串格式
Loguru更喜欢更优雅和强大的{}格式化%，日志记录功能实际上相当于str.format()。
```
logger.info（"如果你正在使用Python {}，当然更喜欢{feature}！"，3.6，feature = "f-strings"）
```
## 在线程或主要内容中捕获异常
```
@ logger.catch 
def  my_function（x，y，z）：
     ＃error？无论如何它被抓住了！
    return 1  /（x + y + z）
```
## 异步，线程安全，多进程安全
logger默认情况下，添加到所有接收器都是线程安全的。它们不是多进程安全的，但您可以使用enqueue这些消息来确保日志的完整性。如果要进行异步日志记录，也可以使用相同的参数。

```
logger.add（“ somefile.log ”，enqueue = True）
```
## 完整的追溯体系
记录代码中出现的异常对于跟踪错误非常重要，但如果您不知道失败的原因，它就毫无用处。Loguru通过允许显示整个堆栈跟踪（包括变量值）来帮助您识别问题。

```
logger.add("output.log", backtrace=True)  # Set 'False' to avoid leaking sensitive data in prod

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)
```
会显示
```
2018-07-17 01:38:43.975 | ERROR    | __main__:nested:10 - What?!
Traceback (most recent call last, catch point marked):

  File "test.py", line 12, in <module>
    nested(0)
    └ <function nested at 0x7f5c755322f0>

> File "test.py", line 8, in nested
    func(5, c)
    │       └ 0
    └ <function func at 0x7f5c79fc2e18>

  File "test.py", line 4, in func
    return a / b
           │   └ 0
           └ 5

ZeroDivisionError: division by zero
```

## 根据需要进行结构化记录
希望序列化您的日志以便于解析或传递它们吗？使用该serialize参数，每个日志消息将在发送到配置的接收器之前转换为JSON字符串。
```
logger.add（custom_sink_function，serialize = True）
```
## 自定义日志级别
```
new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")

logger.log("SNAKY", "Here we go!")
```


## 给出一个常用的日志配置
并不一定是最好的一个实践，但是通用性很高
```python
from loguru import logger
__logConfig= dict(
    rotation='50MB', #日志翻转，每50M单文件分割一个新日志文件出来
    enqueue=True,  #线程安全选项，不会导致多线程写入日志顺序变乱
    # =======暂时有bug，console 打印日志没问题，但是日志文件会乱码
    # colorize=True, 
    # format="<green>{time}</green> <level>{message}</level>",
    # ==============================================================
    encoding='utf-8',
)
if not os.path.exists(fp):
    os.makedirs(fp, exist_ok=True)
fp = fp+'mylog_{time}.log'
logger.add(fp, **__logConfig)
```
通常来说，我们普通的日志文件就已经配置好了，使用logger已经可以打印和记录log文件，例如：
```python
logger.info("info level log")
```

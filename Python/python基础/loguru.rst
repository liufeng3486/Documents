<h1><a id="loguru_0"></a>loguru日志模块</h1>
<h2><a id="_1"></a>简单实践</h2>
<p>首先，你要安装</p>
<pre><code>pip install loguru
</code></pre>
<p>loguru的主要概念只有一个日志记录器。<br>
为了方便起见，它首先被预先配置并输出到stderr(但这是完全可配置的)。<br>
从loguru导入日志记录器<br>
最简单实践一下：</p>
<pre><code class="language-python"><span class="hljs-keyword">from</span> loguru <span class="hljs-keyword">import</span> logger
logger.info(<span class="hljs-string">"this is so easy!"</span>)
</code></pre>
<p>输出：</p>
<pre><code>2019-01-04 14:15:26.936 | INFO     | __main__:&lt;module&gt;:20 - this is so easy
</code></pre>
<p>是不是比内建logging日志模块简单很多？</p>
<h2><a id="_Handler__Formatter_Filter__19"></a>没有 Handler,  Formatter, Filter: 仅仅一个函数解决所有日志配置</h2>
<p>如何添加处理程序？如何设置日志格式？如何过滤邮件？如何设定水平？<br>
一个答案：add()功能。</p>
<pre><code class="language-python">logger.add（sys.stderr，format = <span class="hljs-string">" {time}  {level}  {message} "</span>，filter = <span class="hljs-string">" my_module "</span>，level = <span class="hljs-string">" INFO "</span>）
</code></pre>
<p>此函数应用于注册接收器，该接收器负责管理使用记录字典进行上下文化的日志消息。接收器可以采用多种形式：简单函数，字符串路径，类文件对象，内置处理程序或自定义类。</p>
<h2><a id="_26"></a>使用旋转/保留/压缩更轻松地进行文件记录</h2>
<p>如果要将记录的消息发送到文件，则只需使用字符串路径作为接收器。为方便起见，它也可以自动定时：</p>
<pre><code class="language-python">logger.add（“ file_ {time} .log ”）
</code></pre>
<p>如果您需要旋转记录器，如果要删除旧日志，或者希望在关闭时压缩文件，也可以轻松配置它。</p>
<pre><code>logger.add（“ file_1.log ”，rotation = “ 500 MB ”）     ＃自动ratate太大的文件 
logger.add（“ file_2.log ”，rotation = “ 12:00 ”）      ＃每天中午创建新文件 
logger.add（“ file_3.log ”，rotation = “ 1周”）     ＃文件太旧后，它会被旋转
logger.add（“ file_X.log ”，retention = “ 10天”）   ＃一段时间后清理
logger.add（“ file_Y.log ”，compression = “ zip ”）     ＃保存一些喜爱的空间
</code></pre>
<h2><a id="_39"></a>使用大括号样式的现代字符串格式</h2>
<p>Loguru更喜欢更优雅和强大的{}格式化%，日志记录功能实际上相当于str.format()。</p>
<pre><code>logger.info（&quot;如果你正在使用Python {}，当然更喜欢{feature}！&quot;，3.6，feature = &quot;f-strings&quot;）
</code></pre>
<h2><a id="_44"></a>在线程或主要内容中捕获异常</h2>
<pre><code>@ logger.catch 
def  my_function（x，y，z）：
     ＃error？无论如何它被抓住了！
    return 1  /（x + y + z）
</code></pre>
<h2><a id="_51"></a>异步，线程安全，多进程安全</h2>
<p>logger默认情况下，添加到所有接收器都是线程安全的。它们不是多进程安全的，但您可以使用enqueue这些消息来确保日志的完整性。如果要进行异步日志记录，也可以使用相同的参数。</p>
<pre><code>logger.add（“ somefile.log ”，enqueue = True）
</code></pre>
<h2><a id="_57"></a>完整的追溯体系</h2>
<p>记录代码中出现的异常对于跟踪错误非常重要，但如果您不知道失败的原因，它就毫无用处。Loguru通过允许显示整个堆栈跟踪（包括变量值）来帮助您识别问题。</p>
<pre><code>logger.add(&quot;output.log&quot;, backtrace=True)  # Set 'False' to avoid leaking sensitive data in prod

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception(&quot;What?!&quot;)

nested(0)
</code></pre>
<p>会显示</p>
<pre><code>2018-07-17 01:38:43.975 | ERROR    | __main__:nested:10 - What?!
Traceback (most recent call last, catch point marked):

  File &quot;test.py&quot;, line 12, in &lt;module&gt;
    nested(0)
    └ &lt;function nested at 0x7f5c755322f0&gt;

&gt; File &quot;test.py&quot;, line 8, in nested
    func(5, c)
    │       └ 0
    └ &lt;function func at 0x7f5c79fc2e18&gt;

  File &quot;test.py&quot;, line 4, in func
    return a / b
           │   └ 0
           └ 5

ZeroDivisionError: division by zero
</code></pre>
<h2><a id="_96"></a>根据需要进行结构化记录</h2>
<p>希望序列化您的日志以便于解析或传递它们吗？使用该serialize参数，每个日志消息将在发送到配置的接收器之前转换为JSON字符串。</p>
<pre><code>logger.add（custom_sink_function，serialize = True）
</code></pre>
<h2><a id="_101"></a>自定义日志级别</h2>
<pre><code>new_level = logger.level(&quot;SNAKY&quot;, no=38, color=&quot;&lt;yellow&gt;&quot;, icon=&quot;🐍&quot;)

logger.log(&quot;SNAKY&quot;, &quot;Here we go!&quot;)
</code></pre>
<h2><a id="_109"></a>给出一个常用的日志配置</h2>
<p>并不一定是最好的一个实践，但是通用性很高</p>
<pre><code class="language-python"><span class="hljs-keyword">from</span> loguru <span class="hljs-keyword">import</span> logger
__logConfig= dict(
    rotation=<span class="hljs-string">'50MB'</span>, <span class="hljs-comment">#日志翻转，每50M单文件分割一个新日志文件出来</span>
    enqueue=<span class="hljs-keyword">True</span>,  <span class="hljs-comment">#线程安全选项，不会导致多线程写入日志顺序变乱</span>
    <span class="hljs-comment"># =======暂时有bug，console 打印日志没问题，但是日志文件会乱码</span>
    <span class="hljs-comment"># colorize=True, </span>
    <span class="hljs-comment"># format="&lt;green&gt;{time}&lt;/green&gt; &lt;level&gt;{message}&lt;/level&gt;",</span>
    <span class="hljs-comment"># ==============================================================</span>
    encoding=<span class="hljs-string">'utf-8'</span>,
)
<span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> os.path.exists(fp):
    os.makedirs(fp, exist_ok=<span class="hljs-keyword">True</span>)
fp = fp+<span class="hljs-string">'mylog_{time}.log'</span>
logger.add(fp, **__logConfig)
</code></pre>
<p>通常来说，我们普通的日志文件就已经配置好了，使用logger已经可以打印和记录log文件，例如：</p>
<pre><code class="language-python">logger.info(<span class="hljs-string">"info level log"</span>)
</code></pre>

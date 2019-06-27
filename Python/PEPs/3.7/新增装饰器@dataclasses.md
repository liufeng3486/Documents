## PEP 557 Data Classes

|PEP编号:|557|
|:----|:----|
| 标题：     | Data Classes|
| 作者：      | Eric V. Smith <eric at trueblade.com>   |
| 状态 :       |    Final   |
| 类型：        |    Standards Track   |
| 创建时间：        |    2017-06-02   |
| Python版本：        |    3.7   |
| 上传历史：        | 2017-02-08, 2017-11-25, 2017-11-30, 2017-12-01, 2017-12-02, 2018-01-06, 2018-03-04 |
| 决议：        |    https://mail.python.org/pipermail/python-dev/2017-December/151034.html   |

内容
+ 审阅人员注意
+ 摘要
+ 原理
+ 规范
    + Field对象
    + post-init处理
    + 类变量
    + Init-only变量
    + Frozen实例
    + 继承
    + default_factory函数
    + 可变默认值
    + 模块级辅助函数
+ 讨论
    + python-ideas讨论
    + 支持自动设置__slots__?

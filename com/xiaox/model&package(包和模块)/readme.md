## 包
python中包类似于windows中的目录，但是和目录不同的是每个包中都必须含有一个`__init__.py`文件，不管这个`__init__.py`文件是不是空文件
## 模块
python中一个模块就是一个`.py`文件
## 导入模块的几种方式
```
import math
```
### 使用pow模块
```
math.pow(2,1)
```
```
from math import pow
```
### 使用pow模块
```
pow(2,1)
```
```
from math import pow as power
```
### 使用pow模块
```
power(2,1)
```
## 动态导入
利用导入异常可以动态导入包，兼容python版本
```
try:
    import json
except ImportError:
    import simplejson

print json.dumps({'python':2.7})
```
`simplejson`是python之前的json处理模块，python2.7之后是`json`，利用导入异常就可以兼容两种版本的代码

## `__future__`
当python新版本引入新的功能时，旧版本不支持的功能会被添加到`__future__`中，在旧版本中导入`__future__`中内容，就可以在旧版本中测试新版本的内容  
例如python3.x中`/`得到浮点数，而python2.x中是整数，在python2.x中将`/`转化为浮点数，可以：
```
from __future__ import division
print 10/3
```
## python安装第三方模块
### `pip`（内置，推荐）
```
pip install model_name
```
### `eazy_install`

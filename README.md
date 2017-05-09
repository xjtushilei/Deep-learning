# 深度学习

记录自己的深度学习历程！

# powershell

设置执行脚本权限 `set-ExecutionPolicy RemoteSigned` 

之后放弃了powershell，改用cmder，很好用！

#　安装

## 虚拟环境

 virtualenv --no-site-packages  tensorflow_env （不适用系统的包）
 
 active使用激活，或者在pycharm中配置interpreter（解释器）

## 换源-linux下

当前用户：.pip/pip.conf里增加

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```


## 换源安装TensorFlow

由于在自己电脑上进行测试，所以用cpu版本

如果换源过，可以去掉-i后面的源

 pip install --upgrade tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple
 
 pip最新版推荐https的源
 
## linux下安装keras（请自己配置好cuda等，无gpu请忽略）

需要首先安装TensorFlow，由于有四个Titan Gpu，所以安装gpu版本TensorFlow,并顺带安装了一些其他的工具包

source tensorflow_env/bin/activate

pip install --upgrade tensorflow-gpu -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install -U --pre numpy scipy matplotlib scikit-learn scikit-image -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -U --pre scipy  -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install -U --pre keras -i https://pypi.tuna.tsinghua.edu.cn/simple


## windows 安装keras记录（先安装windows版本TensorFlow）

这样开车方便多了。

1.安装windows版本的numpy和mkl，注意选择python版本和系统

 下载地址：http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

2.安装windows版本的scipy，注意选择python版本和系统

 下载地址：http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
 
3.安装keras

pip install -U --pre keras -i https://pypi.tuna.tsinghua.edu.cn/simple

## 其他

- psycopg2   postgresql的驱动
- pymysql  python3的mysql驱动
 




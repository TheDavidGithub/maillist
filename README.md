# maillist
## 一个通讯录多终端同步的小项目

### 测试步骤：
> 1.安装requirements.txt中的依赖包及其他依赖包  
> 2.从Dump20160903中的文件导入数据到mysql数据库  
> 3.修改配置调试运行

### 需要同时运行以下两个命令才能实现双向通道，达到向客户端发送同步消息的目的：
> python manage.py runworker -v2  
> daphne maillist.asgi:channel_layer --port 8000 --bind 0.0.0.0 -v2

### 请自行修改端口号等参数。

### 最后在浏览器多个窗口打开类似下面的链接即可看到效果：
> http://127.0.0.1:8000/

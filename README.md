# cmdb-
基于python+django制作的cmdb管理平台，集成了ansible、服务树、celery异步处理等功能
基于centos7+python3.7+django2.1.5+ansible2.8.6+celery4.3.0 运维管理系统-开发中，目前实现功能：用户和用户组管理、资产管理、集成ansible、文件上传下载（实现了注册用户头像上传）、celery任务编排，前后端分离，xadmin后台管理。
1、编译器选择 
     vscode
2、 切换到虚拟环境
```
pip install pipenv    
#linux使用pip3安装
pipenv shell 
```
3、安装依赖环境
```
pip  install -r requirements.txt
```
4、数据库
这里使用的django自带的sqlite3
项目迁移的时候可以将数据一起带走
如果不想使用自带数据库可以在setting中设置一下
```
将之前设置的DATABASES注释掉
DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名',
        'USER': '用户名',
        'PASSWORD': '密码自设',
        'HOST': '主机名',
        'PORT': '3306',
    }
}
-----------------------------------------------
执行
python manage.py makemigrations   #数据迁移
python manage.py migrate  #数据映射
```
项目结构
![image.png](https://upload-images.jianshu.io/upload_images/18766817-1cc3eb5bde0e0bd9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

xadmin展示
![xadmin](https://upload-images.jianshu.io/upload_images/18766817-9e16fe354a621496.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


下面截图数据均以xadmin后台管理添加

用户注册

![用户注册](https://upload-images.jianshu.io/upload_images/18766817-2a1605c939561d06.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![用户登录](https://upload-images.jianshu.io/upload_images/18766817-e500a901358fa9aa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

首页展示
![image.png](https://upload-images.jianshu.io/upload_images/18766817-d142a2e4178e3a44.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

资产信息展示
![资产信息](https://upload-images.jianshu.io/upload_images/18766817-a975f457dedef99a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![资产信息分页](https://upload-images.jianshu.io/upload_images/18766817-daaac5be3a34b506.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![服务器信息](https://upload-images.jianshu.io/upload_images/18766817-5cabe685b73c04b0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


Ansible集成
![推送公钥](https://upload-images.jianshu.io/upload_images/18766817-05499301fa44faab.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![批量执行](https://upload-images.jianshu.io/upload_images/18766817-237ab9c11988e4f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>ansible使用的是异步执行操作 需要有异步存储redis和执行者消息队列rabbitmq
是使用的docker容器起的两个进程

服务树
![服务树展示](https://upload-images.jianshu.io/upload_images/18766817-1e425b9eed97d7bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


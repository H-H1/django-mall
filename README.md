# django-mall

# 1.系统需要
1. Django2.4
2. python3.7.4
3. centos 7以上

# 2.下载宝塔

  >yum update
  >
  >yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh &&sh install.sh
  >
  >修改宝塔登陆面板地址和用户密码

## 	2.1软件商店下载插件

1. nginx 1.18

2. mysql5.7

3. redis

4. python项目管理器

5. docker

   ## 2.2宝塔上添加域名站点，以及使用到的端口(如mysql 3366 等)，并给服务器是添加A记录和放行端口

   ![image-20210713122155293](C:\Users\黄延中\AppData\Roaming\Typora\typora-user-images\image-20210713122155293.png)

   ## 2.3python项目管理器中下载python3.7.4，并创建django项目

   ![image-20210713121406783](C:\Users\黄延中\AppData\Roaming\Typora\typora-user-images\image-20210713121406783.png)

   ## 2.4数据库选项导入sql文件，复制密码到setting.dev的mysql配置，并修改用户

   ![image-20210713122117836](C:\Users\黄延中\AppData\Roaming\Typora\typora-user-images\image-20210713122117836.png)

   ## 2.激活并进入虚拟环境：

   >source 虚拟环境目录/bin/activate  

# 3.运行程序 

  >python mange.py runserver  端口


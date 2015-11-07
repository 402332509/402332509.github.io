
# **Nagios - 源码安装Nagios Core手册**


###**目的**
本文档详细介绍了如何从源码安装Nagios Core和Nagios Plugins到CentOS和Ubuntu服务器上。

###**阅读对象**
本文档适用于任何想要从源码安装Nagios Core的用户

###**准备工作**
Ubuntu用户需要获取root权限，下面的命令可用来切换到root帐号
```
sudo -i
```
需要下载的安装包取决于你是何种操作系统。
RHEL/CentOS用户：
```
yum install -y wget httpd php gcc glibc glibc-common gd gd-devel make net-snmp
```
Ubuntu用户：
```
sudo apt-get install wget build-essential apache2 php5-gd libgd2-xpm libgd2-xpm-dev libapache2-modphp5
```
###**下载Nagios Core和Nagios Plugins压缩包**
所有系统都可以用下面的命令进行下载，这会下载Nagios Core和所需的插件
```
cd /tmp
wget http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-4.0.4.tar.gz
wget http://nagios-plugins.org/download/nagios-plugins-2.0.tar.gz
```
###**添加Nagios用户和组**
给运行Nagios程序添加合适的用户和组
```
useradd nagios
groupadd nagcmd
usermod -a -G nagcmd nagios
```
###**Nagios Core安装**
```
tar zxvf nagios-4.0.4.tar.gz
tar zxvf nagios-plugins-2.0.tar.gz
```
切换到解压后的文件目录
```
cd nagios-4.0.4
RHEL/CentOS系统：
./configure --with-command-group=nagcmd
Ubuntu系统：
./configure --with-nagios-group=nagios --with-command-group=nagcmd -–with-mail=/usr/bin/sendmail
```
所有系统：
```
make all
make install
make install-init
make install-config
make install-commandmode
make install-webconf
cp -R contrib/eventhandlers/ /usr/local/nagios/libexec/
chown -R nagios:nagios /usr/local/nagios/libexec/eventhandlers
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
/etc/init.d/nagios start
```
RHEL/CentOS系统：
```
/etc/init.d/httpd start
```
###**创建Web登录帐号**
```
htpasswd –c /usr/local/nagios/etc/htpasswd.users nagiosadmin
```
###**Nagios Plugin安装**
```
cd /tmp/nagios-plugins-2.0
./configure --with-nagios-user=nagios --with-nagios-group=nagios
make
make install
```
###**Nagios服务安装**
下面的命令会在系统启动时创建Nagios守护进程
```
chkconfig --add nagios
chkconfig --level 35 nagios on
chkconfig --add httpd
chkconfig --level 35 httpd on
```
Ubuntu系统：
```
ln -s /etc/init.d/nagios /etc/rcS.d/S99nagios
```
###**Nagios Web页面**
上述流程执行正常后，就可以从浏览器打开Web页面了
```http://<your.nagios.server.ip>/nagios```
###**结束**
如有疑问，可以咨询`Harry.Liu`


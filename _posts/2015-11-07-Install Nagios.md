

---
date: 2015-11-06 18:31:06
layout: post
title: 源码安装Nagios Core手册
thread: 120
categories: 运维
tags: Nagios
---


# **Nagios - 源码安装Nagios Core手册**


###**目的**
本文档详细介绍了如何从源码安装Nagios Core和Nagios Plugins到CentOS和Ubuntu服务器上。

###**阅读对象**
本文档适用于任何想要从源码安装Nagios Core的用户

###**准备工作**
Ubuntu用户需要获取root权限，下面的命令可用来切换到root帐号
{% highlight java %}
sudo -i
{% endhighlight %}
需要下载的安装包取决于你是何种操作系统。
RHEL/CentOS用户：
{% highlight java %}
yum install -y wget httpd php gcc glibc glibc-common gd gd-devel make net-snmp
{% endhighlight %}
Ubuntu用户：
{% highlight java %}
sudo apt-get install wget build-essential apache2 php5-gd libgd2-xpm libgd2-xpm-dev libapache2-modphp5
{% endhighlight %}
###**下载Nagios Core和Nagios Plugins压缩包**
所有系统都可以用下面的命令进行下载，这会下载Nagios Core和所需的插件
{% highlight java %}
cd /tmp
wget http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-4.0.4.tar.gz
wget http://nagios-plugins.org/download/nagios-plugins-2.0.tar.gz
{% endhighlight %}
###**添加Nagios用户和组**
给运行Nagios程序添加合适的用户和组
{% highlight java %}
useradd nagios
groupadd nagcmd
usermod -a -G nagcmd nagios
{% endhighlight %}
###**Nagios Core安装**
{% highlight java %}
tar zxvf nagios-4.0.4.tar.gz
tar zxvf nagios-plugins-2.0.tar.gz
{% endhighlight %}
切换到解压后的文件目录
{% highlight java %}
cd nagios-4.0.4
RHEL/CentOS系统：
./configure --with-command-group=nagcmd
Ubuntu系统：
./configure --with-nagios-group=nagios --with-command-group=nagcmd -–with-mail=/usr/bin/sendmail
{% endhighlight %}
所有系统：
{% highlight java %}
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
{% endhighlight %}
RHEL/CentOS系统：
{% highlight java %}
/etc/init.d/httpd start
{% endhighlight %}
###**创建Web登录帐号**
{% highlight java %}
htpasswd –c /usr/local/nagios/etc/htpasswd.users nagiosadmin
{% endhighlight %}
###**Nagios Plugin安装**
{% highlight java %}
cd /tmp/nagios-plugins-2.0
./configure --with-nagios-user=nagios --with-nagios-group=nagios
make
make install
{% endhighlight %}
###**Nagios服务安装**
下面的命令会在系统启动时创建Nagios守护进程
{% highlight java %}
chkconfig --add nagios
chkconfig --level 35 nagios on
chkconfig --add httpd
chkconfig --level 35 httpd on
{% endhighlight %}
Ubuntu系统：
{% highlight java %}
ln -s /etc/init.d/nagios /etc/rcS.d/S99nagios
{% endhighlight %}
###**Nagios Web页面**
上述流程执行正常后，就可以从浏览器打开Web页面了
{% highlight java %}http://<your.nagios.server.ip>/nagios{% endhighlight %}
###**结束**
如有疑问，可以咨询`Harry.Liu`


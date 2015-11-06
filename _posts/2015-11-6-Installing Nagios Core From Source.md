

---
date: 2015-11-06 18:31:06
layout: post
title: Դ�밲װNagios Core�ֲ�
thread: 120
categories: ��ά
tags: Nagios
---


# **Nagios - Դ�밲װNagios Core�ֲ�**


###**Ŀ��**
���ĵ���ϸ��������δ�Դ�밲װNagios Core��Nagios Plugins��CentOS��Ubuntu�������ϡ�

###**�Ķ�����**
���ĵ��������κ���Ҫ��Դ�밲װNagios Core���û�

###**׼������**
Ubuntu�û���Ҫ��ȡrootȨ�ޣ����������������л���root�ʺ�
{% highlight shell%}
sudo -i
{% endhighlight %}
��Ҫ���صİ�װ��ȡ�������Ǻ��ֲ���ϵͳ��
RHEL/CentOS�û���
{% highlight shell%}
yum install -y wget httpd php gcc glibc glibc-common gd gd-devel make net-snmp
{% endhighlight %}
Ubuntu�û���
{% highlight shell%}
sudo apt-get install wget build-essential apache2 php5-gd libgd2-xpm libgd2-xpm-dev libapache2-modphp5
{% endhighlight %}
###**����Nagios Core��Nagios Pluginsѹ����**
����ϵͳ�����������������������أ��������Nagios Core������Ĳ��
{% highlight shell%}
cd /tmp
wget http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-4.0.4.tar.gz
wget http://nagios-plugins.org/download/nagios-plugins-2.0.tar.gz
{% endhighlight %}
###**���Nagios�û�����**
������Nagios������Ӻ��ʵ��û�����
{% highlight shell%}
useradd nagios
groupadd nagcmd
usermod -a -G nagcmd nagios
{% endhighlight %}
###**Nagios Core��װ**
{% highlight shell%}
tar zxvf nagios-4.0.4.tar.gz
tar zxvf nagios-plugins-2.0.tar.gz
{% endhighlight %}
�л�����ѹ����ļ�Ŀ¼
{% highlight shell%}
cd nagios-4.0.4
RHEL/CentOSϵͳ��
./configure --with-command-group=nagcmd
Ubuntuϵͳ��
./configure --with-nagios-group=nagios --with-command-group=nagcmd -�Cwith-mail=/usr/bin/sendmail
{% endhighlight %}
����ϵͳ��
{% highlight shell%}
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
RHEL/CentOSϵͳ��
{% highlight shell%}
/etc/init.d/httpd start
{% endhighlight %}
###**����Web��¼�ʺ�**
{% highlight shell%}
htpasswd �Cc /usr/local/nagios/etc/htpasswd.users nagiosadmin
{% endhighlight %}
###**Nagios Plugin��װ**
{% highlight shell%}
cd /tmp/nagios-plugins-2.0
./configure --with-nagios-user=nagios --with-nagios-group=nagios
make
make install
{% endhighlight %}
###**Nagios����װ**
������������ϵͳ����ʱ����Nagios�ػ�����
{% highlight shell%}
chkconfig --add nagios
chkconfig --level 35 nagios on
chkconfig --add httpd
chkconfig --level 35 httpd on
{% endhighlight %}
Ubuntuϵͳ��
{% highlight shell%}
ln -s /etc/init.d/nagios /etc/rcS.d/S99nagios
{% endhighlight %}
###**Nagios Webҳ��**
��������ִ�������󣬾Ϳ��Դ��������Webҳ����
{% highlight shell%}http://<your.nagios.server.ip>/nagios{% endhighlight %}
###**����**
�������ʣ�������ѯ`Harry.Liu`












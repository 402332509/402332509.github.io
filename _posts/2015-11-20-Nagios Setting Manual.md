---
date: 2015-10-18 16:58:39
layout: post
title: Nagios配置手册
thread: 136
categories: 运维
tags: nagios
---

#Nagio 配置手册

Nagios配置主目录：/usr/local/nagios/etc/
主要的配置文件是：/usr/local/nagios/etc/nagios.cfg
在这个文件里我们可以扩展配置文件，这里系统自带了几个配置文件，我们简单介绍一下:

{% highlight python %}
#命令配置，添加新的脚本时须在此定义
cfg_file=/usr/local/nagios/etc/objects/commands.cfg
#联系人配置，定义联系人
cfg_file=/usr/local/nagios/etc/objects/contacts.cfg
#时间段配置，可以用来设置接受报警信息的时间段
cfg_file=/usr/local/nagios/etc/objects/timeperiods.cfg
#模版配置，把相同的配置项提取成一个个模版，在定义新的配置时可以继承这些模版
cfg_file=/usr/local/nagios/etc/objects/templates.cfg
{% endhighlight %}

配置主机和组

{% highlight python %}
define host{
        use				linux-server            # 使用的模版，这个主机会继承模版里所有的配置
        host_name		beta1					# 主机名
        alias			beta1					# 别名
        address			192.168.221.201			# IP地址
        }

define hostgroup{
        hostgroup_name  beta-servers			# 组名
        alias           Beta Servers			# 别名
        members         beta1					# 组成员，多个用逗号隔开
        }
{% endhighlight %}

		
配置服务

{% highlight python %}
define service{
        use                             local-service		#使用的模版，这个服务会继承模版里所有的配置
        host_name                       beta1				#要检查的主机名
        service_description             platformAPI			#服务描述，web页面展示的服务名
		#check_command 指定命令和参数，用!分隔。这个例子中，我们指定给http://192.168.1.10:8080/nagios_test.jsp发送http请求，检查返回的结果
        check_command                   check_tomcat!192.168.1.10!8080!/nagios_test.jsp
        }
{% endhighlight %}
		
配置命令

{% highlight python %}
define command{
        command_name    check_tomcat			#命令名称
        command_line    /usr/local/nagios/libexec/check_http -I $ARG1$ -p $ARG2$ -u $ARG3$ -e 200	# 命令行
			# 这里用的是nagios plugins带的插件，其实就是一个shell脚本
			# command_line 定义里有一些变量：$ARG1，$ARG2$，$ARG3$。到Nagios实际执行的时候，它们都会被替换成实际的值
			# 其中$ARG1，$ARG2和$ARG3$会被替换成service里定义处指定的参数
			# 在这个例子中，这三个参数分别用来指定tomcat服务的IP地址，端口号和http请求路径，-e 200 表示http返回200时为正常
        }
{% endhighlight %}














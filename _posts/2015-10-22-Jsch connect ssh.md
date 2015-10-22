---
date: 2015-10-22 16:58:39
layout: post
title: Jsch连接ssh异常
thread: 110
categories: 异常
tags: java
---


我在尝试使用Jsch来建立ssh连接时，我的代码出现了如下异常：

{% highlight java %}
com.jcraft.jsch.JSchException: UnknownHostKey: mywebsite.com. 
RSA key fingerprint is 22:fb:ee:fe:18:cd:aa:9a:9c:78:89:9f:b4:78:75:b4
{% endhighlight %}


我不知道怎么验证这个key，下面是我的代码：

{% highlight java %}
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.Session;

public class ssh{
  public static void main(String[] arg){

    try{
       JSch jsch = new JSch();

       //create SSH connection
       String host = "mywebsite.com";
       String user = "username";
       String password = "123456";

       Session session = jsch.getSession(user, host, 22);
       session.setPassword(password);
       session.connect();

     }
     catch(Exception e){
       System.out.println(e);
    } 
  }
}
{% endhighlight %}


解决方案：添加Jsch配置来关闭StrictHostKeyChecking（强制检查key），添加如下代码后问题解决。


{% highlight java %}
java.util.Properties config = new java.util.Properties(); 
config.put("StrictHostKeyChecking", "no");
session.setConfig(config);
{% endhighlight %}


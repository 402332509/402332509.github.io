---
date: 2015-10-22 16:58:39
layout: post
title: Jsch����ssh�쳣
thread: 110
categories: �쳣
tags: java
---


���ڳ���ʹ��Jsch������ssh����ʱ���ҵĴ�������������쳣��

{% highlight java %}
com.jcraft.jsch.JSchException: UnknownHostKey: mywebsite.com. 
RSA key fingerprint is 22:fb:ee:fe:18:cd:aa:9a:9c:78:89:9f:b4:78:75:b4
{% endhighlight %}


�Ҳ�֪����ô��֤���key���������ҵĴ��룺

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


������������Jsch�������ر�StrictHostKeyChecking��ǿ�Ƽ��key����������´������������


{% highlight java %}
java.util.Properties config = new java.util.Properties(); 
config.put("StrictHostKeyChecking", "no");
session.setConfig(config);
{% endhighlight %}


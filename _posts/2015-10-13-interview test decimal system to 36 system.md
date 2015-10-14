---
date: 2015-10-12 16:58:39
layout: post
title: 十进制转36进制
thread: 103
categories: 算法
tags: 进制转换
---

我的代码：欢迎吐槽

{% highlight java %}
import java.util.*;

public class Main {
	static Map<Integer,String> map = new HashMap<Integer,String>();
	public static void main(String[] args) {
		initMap();
		System.out.println(tenTo36(100));
	}
	/**
	 * 将字符A-Z用10进制数表示
	 */
	public static void initMap(){
		for(int i=0;i<10;i++){
			map.put(i,""+i);
		}
		for(int i=10;i<36;i++){
			map.put(i, ""+(char)(i+55));
		}
	}
	/**
	 * 十进制转16进制
	 * @param num10
	 * @return
	 */
	public static String tenTo36(int num10){
		StringBuffer num36= new StringBuffer();
		for(;(num10/36)!=0;num10/=36){
			num36.insert(0,map.get(num10%36));
		}
		num36.insert(0,num10);
		return num36.toString();
	}

}
{% endhighlight %}

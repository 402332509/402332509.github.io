---
date: 2016-12-14 00:22:05
layout: post
title: 使用自定义样式
thread: 1001
categories: 日志
tags: Salesforce, Visualforce Pages
---


# 使用自定义样式
使用 `<apex:stylesheet>` 标签或静态HTML来放置你自己的样式表或样式。
HTML中，你可以定义内置CSS代码，就像普通的HTML页面那样。

```
<apex:page>
    <style type="text/css">
        p { font-weight: bold; }
    </style>

    <p>This is some strong text!</p>
</apex:page>
```

下面这个例子引用了一个在静态资源中定义了的样式表。首先，创建一个样式表并上传到静态资源中，取名为customCSS。

```
h1 { color: #f00; }
p { background-color: #eec; }
newLink { color: #f60; font-weight: bold; }
```

然后，创建一个引用到该静态资源的页面。

```
<apex:page showHeader="false">
    <apex:stylesheet value="{!$Resource.customCSS}" />
    <h1>Testing Custom Stylesheets</h1>
    <p>This text could go on forever...<br/><br/>
       But it won't!</p>

    <apex:outputLink value="http://www.salesforce.com" styleClass="newLink">
        Click here to switch to www.salesforce.com
    </apex:outputLink>
</apex:page>
```


- - - -
注意：如果你不使用Salesforce样式，你可以通过取消加载标准的Salesforce样式表来缩放你的页面大小。要取消加载，将 `<apex:page>` 内的 `standardStylesheets` 属性设置为false。

```
<apex:page standardStylesheets="false">
    <!-- page content here -->
</apex:page>
```

如果你不加载Salesforce样式表，需要用到这些样式的组件不会正确地显示。
- - - -


生成HTML的Visualforce组件有style或styleClass属性。这些属性允许你使用你自己的样式和组件上的样式类来控制HTML的页面效果。style允许你直接在组件上设置样式，同时styleClass可以添加定义在其他地方的类。举个例子，下面的代码设置了 `<apex:outputText>` 的样式。

```
<apex:page>

    <style type="text/css">
        .asideText { font-style: italic; }
    </style>

    <apex:outputText style="font-weight: bold;" 
        value="This text is styled directly."/>

    <apex:outputText styleClass="asideText" 
        value="This text is styled via a stylesheet class."/>

</apex:page>
```

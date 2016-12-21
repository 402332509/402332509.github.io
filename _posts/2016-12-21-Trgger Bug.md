---
date: 2016-12-21 10:30:39
layout: post
title: System.SObjectException: DML statement cannot operate on trigger.new or trigger.old
thread: 1003
categories: 日志
tags: Salesforce, Exception
---

在trigger的before时，不需要也不能对当前对象进行update, insert或delete操作！
以为在before之后会自动执行上述操作。

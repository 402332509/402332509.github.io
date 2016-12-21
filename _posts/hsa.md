---
date: 2016-12-21 10:43:00
layout: post
title: Trigger Bug
thread: 1003
categories: 日志
tags: Salesforce Apex Bug
---

###System.SObjectException: DML statement cannot operate on trigger.new or trigger.old



在trigger的before时，不需要也不能对当前对象进行update, insert或delete操作！
以为在before之后会自动执行上述操作。

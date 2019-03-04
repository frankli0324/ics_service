# TimetableService

[![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/frankli0324/TimetableService)

目前部署于http://ics.qwer.design

## 这个东西能干什么？

通过大部分设备自带的订阅账户功能将西安电子科技大学的课表导入到手机自带的日历

## 原理是什么？

通过爬取来自一站式服务大厅(ehall)我的课表应用的数据，生成课表并进行持久化存储

## Getting Started

//TODO
[请先参阅SCNU的使用说明](https://i.scnu.edu.cn/ical/doc)

## License Agreement

使用本服务，代表您已理解并允许本服务使用您的西电统一认证所需登陆信息  
本服务保证只对登陆信息进行转发，而不进行存储，只将其用作以下用处:
用户名: 登陆一站式服务大厅, 在服务端存储获取到的日历信息(作为文件名)
密码: 仅用作登陆，且仅使用一次，之后可通过生成的Token直接访问获取到的日历文件

## 备注: 如何保证我的密码不被泄漏

不能保证。  
因为不仅本页面没有https，就连ehall一站式服务大厅也没有https。  
但是由于本页面是开源的。你可以自己按照原样部署一份。  
要是觉得不安全，又嫌自己部署太麻烦，那你可以使用[xidian-scripts](https://github.com/xdlinux/xidian-scripts)获取日历文件(.ics)自行导入。对IOS用户，目前尚未找到能直接导入ics的方式。

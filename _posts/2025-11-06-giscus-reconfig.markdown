---
layout: post
title: "重新配置Giscus测试"
subtitle: "使用标准配置重新设置评论系统"
date: 2025-11-06 22:00:00
author: "荣正"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - 测试
    - Giscus
    - 重新配置
---

## 重新配置Giscus测试页面

这个页面使用了重新配置的Giscus设置。

### 测试步骤：
1. 检查页面底部是否正常显示Giscus评论框
2. 尝试发表一条测试评论
3. 检查评论是否能正常显示
4. 查看浏览器控制台是否有错误信息

### 可能的问题原因：
1. **Category ID错误** - GitHub Discussions的分类ID与配置不匹配
2. **Repository权限问题** - 仓库设置可能阻止了评论
3. **映射方式问题** - pathname映射可能有问题
4. **JavaScript冲突** - 其他脚本可能干扰了Giscus

请在下方测试评论功能！
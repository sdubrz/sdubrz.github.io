---
layout: post
title: "Giscus权限测试"
subtitle: "解决"Unable to create discussion"错误"
date: 2025-11-06 23:00:00
author: "荣正"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - 权限测试
    - Giscus
    - 调试
---

## Giscus权限问题排查

当您看到"Unable to create discussion"错误时，通常是以下原因：

### 可能的原因：

1. **GitHub仓库未启用Discussions功能**
   - 需要在仓库设置中启用Discussions

2. **Giscus App权限不足**
   - 需要安装并授权Giscus GitHub App

3. **Category配置错误**
   - Category ID与实际的讨论分类不匹配

4. **仓库权限问题**
   - 仓库可能是私有的或有访问限制

### 解决步骤：

#### 第一步：检查仓库设置
请访问：[仓库设置](https://github.com/sdubrz/sdubrz.github.io/settings)
确保：
- ✅ Discussions功能已启用
- ✅ 仓库是公开的

#### 第二步：安装Giscus App
访问：[Giscus App安装页面](https://github.com/apps/giscus)
- 点击"Install"或"Configure"
- 选择您的仓库或"All repositories"
- 确保权限包括"Discussions"

#### 第三步：重新配置Giscus
访问：[Giscus配置页面](https://giscus.app/zh-CN)
- 输入您的仓库：sdubrz/sdubrz.github.io
- 选择正确的讨论分类
- 复制生成的配置代码

### 测试评论区：

{% include giscus-test.html %}

---

### 如果仍然有问题：

1. 检查浏览器控制台的错误信息
2. 确认您有仓库的管理员权限
3. 尝试在GitHub Discussions中手动创建一个讨论测试

请按照上述步骤检查并尝试在下方评论！
---
layout: post
title: "Giscus调试页面"
subtitle: "检查Giscus配置参数"
date: 2025-11-06 21:00:00
author: "荣正"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - 调试
    - Giscus
---

## Giscus配置调试

让我们检查Giscus的配置参数：

### 当前配置：
- Repo: {{ site.giscus.repo }}
- Repo ID: {{ site.giscus.repo_id }}
- Category: {{ site.giscus.category }}
- Category ID: {{ site.giscus.category_id }}
- Mapping: {{ site.giscus.mapping }}
- Enable: {{ site.giscus.enable }}
- Lang: {{ site.giscus.lang }}

### 页面信息：
- 页面URL: {{ page.url }}
- 页面路径: {{ page.path }}
- 站点URL: {{ site.url }}

如果您在GitHub Discussions中看到了评论，但在这里看不到，请检查：
1. Category是否正确
2. Mapping方式是否匹配
3. 是否有JavaScript错误
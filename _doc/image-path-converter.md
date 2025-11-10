# 图片路径自动转换插件使用说明

## 功能描述

这个Jekyll插件可以自动转换Typora编辑器生成的相对图片路径，使其在GitHub Pages上正确显示。

## 工作原理

- **Typora编辑时**：图片以相对路径存储，如 `./2025-11-10-Roll_flash.assets/image.png`
- **Jekyll渲染时**：插件自动转换为绝对路径，如 `/_posts/paper/2025-11-10-Roll_flash.assets/image.png`

## 转换规则

对于文件名为 `${file_name}.markdown` 的文章：

### 内容中的图片
```markdown
# Typora格式（输入）
![description](./2025-11-10-Roll_flash.assets/image.png)
![description](2025-11-10-Roll_flash.assets/image.png)

# 自动转换为（输出）
![description](/_posts/paper/2025-11-10-Roll_flash.assets/image.png)
```

### Front Matter中的header-img
```yaml
# Typora格式（输入）
header-img: "./2025-11-10-Roll_flash.assets/image.png"

# 自动转换为（输出）  
header-img: "/_posts/paper/2025-11-10-Roll_flash.assets/image.png"
```

## 使用方式

1. **在Typora中正常编辑**：插入图片时保持默认设置，让Typora创建 `.assets` 目录
2. **提交到GitHub**：直接提交，无需手动修改路径
3. **自动生效**：Jekyll构建时自动转换路径

## 支持的文件

- 所有 `_posts/` 目录下的 `.markdown` 和 `.md` 文件
- 支持嵌套目录，如 `_posts/paper/article.markdown`

## 注意事项

- 图片目录必须命名为 `${文件名}.assets/`
- 插件只处理符合此命名规律的相对路径
- 其他图片路径保持不变
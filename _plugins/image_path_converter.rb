module Jekyll
  class ImagePathConverter
    def self.convert_content(content, post_path)
      # 获取文件名（不带扩展名）
      file_name = File.basename(post_path, File.extname(post_path))
      
      # 获取文件所在的目录路径（相对于_posts）
      post_dir = File.dirname(post_path)
      
      # 转换图片路径规则：
      # 1. ./${file_name}.assets/${image_file_name} -> /${post_dir}/${file_name}.assets/${image_file_name}
      # 2. ${file_name}.assets/${image_file_name} -> /${post_dir}/${file_name}.assets/${image_file_name}
      
      # 处理 ./ 开头的情况
      content = content.gsub(
        /!\[([^\]]*)\]\(\.\/#{Regexp.escape(file_name)}\.assets\/([^)]+)\)/,
        "![\\1](/#{post_dir}/#{file_name}.assets/\\2)"
      )
      
      # 处理直接以文件名开头的情况（没有 ./ 前缀）
      content = content.gsub(
        /!\[([^\]]*)\]\(#{Regexp.escape(file_name)}\.assets\/([^)]+)\)/,
        "![\\1](/#{post_dir}/#{file_name}.assets/\\2)"
      )
      
      content
    end
    
    def self.convert_front_matter(post)
      # 获取文件名（不带扩展名）
      file_name = File.basename(post.relative_path, File.extname(post.relative_path))
      post_dir = File.dirname(post.relative_path)
      
      # 转换 front matter 中的 header-img 路径
      if post.data['header-img'] && post.data['header-img'].match(/^\.?\/#{Regexp.escape(file_name)}\.assets\//)
        post.data['header-img'] = post.data['header-img'].gsub(
          /^\.?\/#{Regexp.escape(file_name)}\.assets\//,
          "/#{post_dir}/#{file_name}.assets/"
        )
      end
    end
  end

  # Hook到Posts的预渲染阶段
  Jekyll::Hooks.register :posts, :pre_render do |post|
    if post.extname == '.markdown' || post.extname == '.md'
      # 转换 front matter 中的图片路径
      ImagePathConverter.convert_front_matter(post)
      # 转换内容中的图片路径
      post.content = ImagePathConverter.convert_content(post.content, post.relative_path)
    end
  end
  
  # 同时处理页面（如果需要的话）
  Jekyll::Hooks.register :pages, :pre_render do |page|
    if (page.extname == '.markdown' || page.extname == '.md') && page.relative_path.start_with?('_posts/')
      page.content = ImagePathConverter.convert_content(page.content, page.relative_path)
    end
  end
end
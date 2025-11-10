Jekyll::Hooks.register :posts, :pre_render do |post|
  # 获取文章的目录路径
  post_dir = File.dirname(post.relative_path)
  post_name = File.basename(post.path, ".*")
  
  # 处理图片路径
  post.content = post.content.gsub(/!\[([^\]]*)\]\(\.\/([^)]+\.assets\/[^)]+)\)/) do |match|
    alt_text = $1
    relative_path = $2
    
    # 构建新的路径：从网站根目录开始的绝对路径
    new_path = "/#{post_dir}/#{relative_path}"
    
    "![#{alt_text}](#{new_path})"
  end
end
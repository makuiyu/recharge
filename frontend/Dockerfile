# 使用轻量级的 Nginx 镜像作为基础镜像
FROM nginx:alpine

# 将前端代码复制到 Nginx 服务器目录
COPY . /usr/share/nginx/html

# 暴露端口 80
EXPOSE 80

# 启动 Nginx 服务器
CMD ["nginx", "-g", "daemon off;"]
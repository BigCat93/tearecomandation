# 个性化茶饮推荐系统

这是一个基于中医体质理论的个性化茶饮推荐系统。系统通过简单的问卷调查，分析用户的体质特点，并为其推荐最适合的茶饮。

## 功能特点

- 基于九种中医体质类型的茶饮推荐
- 响应式设计，支持移动端和桌面端
- 简单直观的用户界面
- 即时推荐结果

## 部署说明

1. 创建 GitHub 仓库
   - 登录您的 GitHub 账号
   - 创建一个新的仓库，命名为 `bigcat93.github.io`
   - 确保仓库是公开的（Public）

2. 克隆仓库到本地
   ```bash
   git clone https://github.com/bigcat93/bigcat93.github.io.git
   ```

3. 将项目文件复制到仓库
   - 将所有文件复制到克隆的仓库目录中

4. 提交并推送代码
   ```bash
   cd bigcat93.github.io
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

5. 等待部署
   - GitHub Pages 会自动部署您的网站
   - 通常需要几分钟时间
   - 部署完成后，您可以通过 https://bigcat93.github.io 访问网站

## 本地开发

如果您想在本地预览网站，只需使用任何 HTTP 服务器即可。例如，使用 Python 的简单 HTTP 服务器：

```bash
python -m http.server 8000
```

然后在浏览器中访问 `http://localhost:8000`

## 技术栈

- HTML5
- CSS3
- JavaScript (ES6+)
- Bootstrap 5
- 响应式设计

## 维护者

- @bigcat93

## 许可证

MIT License 
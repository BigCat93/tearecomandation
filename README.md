# 个性化茶饮推荐系统

![Python Application](https://github.com/yourusername/tearecomandation/workflows/Python%20Application/badge.svg)

这是一个基于Python的个性化茶饮推荐系统，结合中医九种体质理论，为用户提供个性化的茶饮推荐。

## 功能特点

- 中医九种体质知识库
- 个性化茶饮推荐
- 基于决策树和随机森林的分类算法
- 响应式Web界面
- 跨平台兼容

## 安装说明

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/tearecomandation.git
cd tearecomandation
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 创建`.env`文件并设置环境变量：
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
PORT=5000
DEBUG=True
```

5. 运行应用：
```bash
python app.py
```

## 部署到Heroku

1. 安装Heroku CLI并登录：
```bash
heroku login
```

2. 创建Heroku应用：
```bash
heroku create your-app-name
```

3. 设置环境变量：
```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your_secret_key_here
```

4. 部署应用：
```bash
git push heroku main
```

## 系统要求

- Python 3.8+
- 支持现代浏览器

## 使用说明

1. 访问首页，了解中医九种体质基本知识
2. 点击"今天喝什么茶？"开始个性化推荐
3. 填写个人健康数据（约需1分钟）
4. 获取个性化茶饮推荐结果

## 测试

运行测试：
```bash
pytest
```

## 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建Pull Request

## 开源协议

MIT License 